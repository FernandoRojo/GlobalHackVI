var map;
var markers = []
var entries = []
function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        center: {
            lat: 38.6270,
            lng: -90.1994
        },
        zoom: 15
    });
    var json_obj = Get('/shelters/heatdata');
    json_obj = JSON.parse(json_obj);
    json_obj = JSON.parse(json_obj);
    console.log(json_obj);
    for (var i in json_obj) {
	var entry = json_obj[i];
        var place_id = entry["fields"]['place_id'];
        var maxCap = entry["fields"]['maxCap'];
        var currCap = entry["fields"]['currCap'];
        var name = entry["fields"]['Name'];
        var infowindow = new google.maps.InfoWindow();
        var service = new google.maps.places.PlacesService(map);
	entries.push({
	    key:   place_id,
	    value: entry
	});
	service.getDetails({placeId: place_id}, 
			   function(place, status) {
			       if (status === google.maps.places.PlacesServiceStatus.OK) {
				   addMarker(place);
			       }
			   });
	}
    console.log(entries);
    console.log(markers);
    for (i in markers){
	 marker = markers[i];
	 entry = entries[i];
	 console.log(i + " : " + entry);
    
    }
 }

 function addMarker(place){
     var image = 'http://findicons.com/files/icons/1150/tango/32/go_home.png';
     var marker = new google.maps.Marker({
	 map: map,
	 position: place.geometry.location,
	 icon: image

     });
     infowindow = new google.maps.InfoWindow();
     google.maps.event.addListener(marker, 'click', function() {
	 var addr = place.formatted_address;
	 addr = addr.split(' ').join('+');
	 var url = 'https://www.google.com/maps/dir//' + addr;
	 infowindow.open(map, this);
     });
     alert(String(place.place_id));
     alert(entries);
     markers.push({
	 key:   place.place_id,
	 value: marker
     });
 }
 function Get(yourUrl) {
     var Httpreq = new XMLHttpRequest(); // a new request
     Httpreq.open('GET', yourUrl, false);
     Httpreq.send(null);
     return Httpreq.responseText;
 }

 function filterMarkers(filter){
     for (i in markers.length){
	 markers[i][1].setMap(null);
     }
     if (filter=='showAll'){
	 for (i in markers.length){
	     markers[i][1].setMap(map);
	 }
     }
     else if (filter=='bedsAvailable'){
	 for (i in markers.length){
	     var entry = markers[i][0];
	     if (entry["fields"]["maxCap"]<=entry["fields"]["currCap"])
		 markers[i][1].setMap(map);
	 }
     }
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
