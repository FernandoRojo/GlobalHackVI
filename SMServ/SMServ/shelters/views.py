from django.core import serializers
import googlemaps
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
import plivo, plivoxml
import requests
from django.http import HttpResponse
from flask import Flask, Response
from geopy.geocoders import Nominatim
from geopy.distance import vincenty
from HTMLParser import HTMLParser
from .models import Shelter

app = Flask(__name__)

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("")
    def handle_endtag(self, tag):
        print("")
    def handle_data(self, data):
        if data!=None and self!=None:
            print("", data)

gmaps = googlemaps.Client(key='AIzaSyCmrWI-KUqvpz4Cn38U6hTDP5rDmN2bm4U')
text = ''
shelter_coordinates = []
def find_long_lat(address):
    geolocator = Nominatim()
    location = geolocator.geocode(address,timeout=30)
    if location == None: return None
    latitude, longitude = location.latitude, location.longitude
    return latitude, longitude
app = Flask(__name__)

@csrf_exempt
@app.route("/receive_sms/", methods=['GET','POST'])
def inbound_sms(request):
    # Sender's phone number
    request = request.POST
    from_number = request['From']
    # Receiver's phone number - Plivo number
    to_number = request['To']
    # The text which was received
    text_message = request['Text']
    loc = find_long_lat(text_message)
    best_location = find_best_loc([x.address for x in Shelter.objects.all() if len(x.address)>0], loc)
    
    resp = best_location
    body = directions(best_location,text_message,MyHTMLParser())
    params = {

        'src' : to_number, # Sender's phone number
        'dst' : from_number,
        'callbackUrl': 'http://ec2-54-200-133-41.us-west-2.compute.amazonaws.com:5000/sms/', # URL that is notified by Plivo when a response is available and to which the response is sent
        'callbackMethod' : "POST" # The method used to notify the callbackUrl
}
    # Message added
    body = resp
    r = plivoxml.Response()
    r.addMessage(body, **params)    
    print r.to_xml()
    print {'Address':text_message,'latitude':loc[0],'longitude':loc[1]}
    requests.post('http://ec2-54-200-133-41.us-west-2.compute.amazonaws.com:8002/shelters/heatdata', data ={'Address':text_message,'latitude':loc[0],'longitude':loc[1]})
    return HttpResponse(str(r), content_type="text/xml")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

def find_best_loc(arr, current_loc):
    geolocator = Nominatim()
    pairs = []
    minimum = float('inf')
    best_lat, best_long = None, None
    for i in range(len(arr)):
        print(str(i*100.0/len(arr)) + "%")
        if current_loc != arr[i]:
            d = find_long_lat(arr[i])
            if d:
                dist = vincenty(current_loc,  find_long_lat(arr[i])).meters
            if dist < minimum:
                minimum = dist
                best_location = arr[i]
    return best_location



def directions(current_loc, address, parser):
    now = datetime.now()
    directions_result = gmaps.directions(current_loc, address, mode="walking", departure_time=now)
    directions = parser.feed(directions_result[0]['legs'][0]['steps'][0]['html_instructions'])
    return directions


