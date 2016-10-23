function initMap() {
    var placeDict = grabPlaceVars();
    console.log
    var map = new google.maps.Map(document.getElementById('map'), {
        center: {
            lat: 38.6270,
            lng: -90.1994
        },
        zoom: 15
    });
    var json_obj = Get('/shelters/heatdata');
    for (place_id in placeDict) {
        var infowindow = new google.maps.InfoWindow();
        var service = new google.maps.places.PlacesService(map);

        service.getDetails({
            placeId: place_id // grab placeids from multiple shelters and create markers / id
        }, function(place, status) {
            if (status === google.maps.places.PlacesServiceStatus.OK) {
                var image = 'http://findicons.com/files/icons/1150/tango/32/go_home.png'
                var marker = new google.maps.Marker({
                    map: map,
                    position: place.geometry.location,
                    icon: image
                });
                var addr = place.formatted_address;
                addr = addr.split(' ').join('+');
                var url = 'https://www.google.com/maps/dir//' + addr;
                var contentString = ('<div><strong>' + placeDict[place.place_id][1] + '</strong><br>' +
                    'Beds Available: ' + grabDiff(placeDict[place.place_id][1], json_obj) + '<br>' +
                    place.formatted_address + '<br> <a href=' + url + '>Directions to Here </a><br></div>');
                var infowindow = new google.maps.InfoWindow({
                    content: contentString
                });
                google.maps.event.addListener(marker, 'click', function() {
                    infowindow.open(map, this);
                });
            }
        });
    }
}

function Get(yourUrl) {
    var Httpreq = new XMLHttpRequest(); // a new request
    Httpreq.open('GET', yourUrl, false);
    Httpreq.send(null);
    return Httpreq.responseText;
}


function grabPlaceVars() {
    var toggle = document.getElementById('toggleBed').value;
    var json_obj = Get('/shelters/heatdata');
    json_obj = JSON.parse(json_obj);
    json_obj = JSON.parse(json_obj);
    //console.log(json_obj);
    var placeDict = {};
    console.log(json_obj);
    for (var i in json_obj) {

        var place_id = json_obj[i]["fields"]['place_id'];
        var maxCap = json_obj[i]["fields"]['maxCap'];
        var currCap = json_obj[i]["fields"]['currCap'];
        var name = json_obj[i]["fields"]['Name'];
        var diff = maxCap - currCap;
        console.log(maxCap);
        console.log(currCap);
        console.log('diff ' + [diff, name]);
        //only add beds to the map if availability is > 0 and toggle is on
        if (toggle == 'off' || diff > 0) {
            placeDict[place_id] = [diff, name, i];
        }
    }
    return placeDict;


}

function grabDiff(name, json_obj){
  json_obj = JSON.parse(json_obj);
  json_obj = JSON.parse(json_obj);
  for (var i in json_obj) {
    var name2 = json_obj[i]["fields"]['Name'];
    if ( (name.toLowerCase()) == (name2.toLowerCase())){
      var maxCap = json_obj[i]["fields"]['maxCap'];
      var currCap = json_obj[i]["fields"]['currCap'];
      var diff = maxCap - currCap;
      return (diff);
    }
  }
}

function toggleBeds() {
    console.log(document.getElementById('toggleBed').value);
    var tog = document.getElementById('toggleBed').value;
    if (tog == 'on') {
        (document.getElementById('toggleBed').value = 'off');
    } else {
        document.getElementById('toggleBed').value = 'on';
    }
    initMap();
}
