import googlemaps
from datetime import datetime
import plivo, plivoxml
from flask import Flask, request, make_response
from geopy.geocoders import Nominatim
from geopy.distance import vincenty
from html.parser import HTMLParser
app = Flask(__name__)
@app.route("/receive_sms/", methods=['GET','POST'])
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
    location = geolocator.geocode(address)
    latitude, longitude = location.latitude, location.longitude
    return latitude, longitude
@app.route('/reply_to_sms/',methods=['GET','POST'])
def inbound_sms():
    # Sender's phone number
    from_number = request.values.get('From')
    # Receiver's phone number - Plivo number
    to_number = request.values.get('To')
    # The text which was received
    text_message = request.values.get('Text')
    best_location = find_best_loc(shelter_coordinates, find_long_lat(text_message))
    resp = plivoxml.Response()
    body = directions(best_location)
    params = {
    'src' : '18053992192', # Sender's phone number
    'dst' : '15712550606',
    'callbackUrl': 'http://ec2-54-200-133-41.us-west-2.compute.amazonaws.com:5000/SMS', # URL that is notified by Plivo when a response is available and to which the response is sent
    'callbackMethod' : "POST" # The method used to notify the callbackUrl
    }
    # Message added
    resp.addMessage(body, **params)
    ret_response = make_response(resp.to_xml())
    ret_response.headers["Content-type"] = "text/xml"

    # Prints the XML
    print(resp.to_xml())
    return ret_response
def find_best_loc(arr, current_loc):
    geolocator = Nominatim()
    pairs = []
    minimum = float('inf')
    best_lat, best_long = None, None
    for i in range(len(arr)):
        if current_loc != arr[i]:
            dist = vincenty(find_long_lat(current_loc),  find_long_lat(arr[i])).meters
            if dist < minimum:
                minimum = dist
                best_location = arr[i]
    return best_location
def directions(current_loc, address, parser):
    now = datetime.now()
    directions_result = gmaps.directions(current_loc, address, mode="walking", departure_time=now)
    directions = parser.feed(directions_result[0]['legs'][0]['steps'][0]['html_instructions'])
    return directions
#SEND THE CONTENTS OF receive_sms_find_best back to the user
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
