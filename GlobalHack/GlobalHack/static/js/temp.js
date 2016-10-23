var map;
var markers = {}
var entries = {}
function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        center: {
            lat: 38.6270,
            lng: -90.1994
        },
        zoom: 15
    });
    var json_obj = Get('/shelters/shelterdata');
    json_obj = JSON.parse(json_obj);
    json_obj = JSON.parse(json_obj);
    console.log(json_obj);
    for (var i in json_obj) {
	var entry = json_obj[i];
        var place_id = entry["fields"]['place_id'];
        var maxCap = entry["fields"]['maxCap'];
        var currCap = entry["fields"]['currCap'];
        var name = entry["fields"]['Name'];
        var service = new google.maps.places.PlacesService(map);
	entries[place_id] = entry;
	service.getDetails({placeId: place_id}, 
			   function(place, status) {
			       if (status === google.maps.places.PlacesServiceStatus.OK) {
				   addMarker(place);
			       }
			   });
	}
    console.log(entries);
    console.log(markers);
    
    
 }

 function addMarker(place){
     var image = 'http://findicons.com/files/icons/1150/tango/32/go_home.png';
     var marker = new google.maps.Marker({
	 map: map,
	 position: place.geometry.location,
	 icon: image,
	  animation: google.maps.Animation.DROP
     });
     var infowindow = new google.maps.InfoWindow(
	 {content: getContext(place.place_id)});
     google.maps.event.addListener(marker, 'click', function() {
	 	 infowindow.open(map, this);
	      });
     markers[place.place_id] = marker;
 }
 function Get(yourUrl) {
     var Httpreq = new XMLHttpRequest(); // a new request
     Httpreq.open('GET', yourUrl, false);
     Httpreq.send(null);
     return Httpreq.responseText;
 }

 function filterMarkers(filter){
      for (i in markers){
	 markers[i].setMap(null);
     }
     if (filter=='showAll'){
	 for (i in markers){
	     markers[i].setMap(map);
	 }
     }
     else if (filter=='bedsAvailable'){
	 for (i in markers){
	     var entry = entries[i];
	     if (entry["fields"]["maxCap"]>entry["fields"]["currCap"])
		 markers[i].setMap(map);
	 }
     }
 }

function getContext(place_id){
    var entry = entries[place_id];
    return '<div><strong>' + entry["fields"]["Name"] + '</strong><br>' +
        'Beds Available: ' +  (entry["fields"]["maxCap"]-entry["fields"]["currCap"]) + '<br>' 
    + entry["fields"]["Address"] + '<br> <a href=' + "apple" + '>Directions to Here </a><br></div>';

}
 function toggleBeds(){
     console.log(document.getElementById('toggleBed').value);
     var tog = document.getElementById('toggleBed').value;
     if (tog == 'on'){
	 document.getElementById('toggleBed').value = 'off';
	 filterMarkers('showAll');
     }
     else{
	 document.getElementById('toggleBed').value = 'on';
	 filterMarkers('bedsAvailable');
     }

}
