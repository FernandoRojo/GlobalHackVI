function initMap() {
    var placeDict = grabPlaceVars();
    var map = new google.maps.Map(document.getElementById('map'), {
        center: {
            lat: 38.6270,
            lng: -90.1994
        },
        zoom: 15
    });
    for (place_id in placeDict) {
        console.log('hi');
        console.log(place_id);
        console.log(placeDict[place_id]);
        var infowindow = new google.maps.InfoWindow();
        var service = new google.maps.places.PlacesService(map);

        service.getDetails({
            placeId: place_id // grab placeids from multiple shelters and create markers / id
        }, function(place, status) {
            var beds = placeDict[place_id];
            if (status === google.maps.places.PlacesServiceStatus.OK) {
                var image = 'http://findicons.com/files/icons/1150/tango/32/go_home.png'
                var marker = new google.maps.Marker({
                    map: map,
                    position: place.geometry.location,
                    icon: image,
                    numBeds: beds
                });
                google.maps.event.addListener(marker, 'click', function() {
                    infowindow.setContent('<div><strong>' + place.name + '</strong><br>' +
                        'Beds Available: ' + placeDict[place.place_id] + '<br>' +
                        place.formatted_address + '</div>');
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
    var json_obj = Get('/shelters/heatdata');
    json_obj = JSON.parse(json_obj);
    json_obj = JSON.parse(json_obj);
    var placeDict = {};
    for (var i in json_obj) {
        var place_id = json_obj[i]["fields"]['place_id'];
        var maxCap = json_obj[i]["fields"]['maxCap'];
        var currCap = json_obj[i]["fields"]['currCap'];
        var diff = parseInt(maxCap, 10) - parseInt(currCap, 10);
        console.log('DIFFFF ' + diff);
        //only add beds to the map if availability is > 0
        if (diff > 0) {
            placeDict[place_id] = diff;
        }
    }
    return placeDict;


}
