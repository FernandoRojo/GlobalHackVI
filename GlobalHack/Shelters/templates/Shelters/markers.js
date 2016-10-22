function initMap() {
  var place_ids = ['ChIJ9ycCtziz2IcRacXnN3lsuks', 'ChIJw6Mt3iNL34cRM6Nk9YQtae8'];
    var map = new google.maps.Map(document.getElementById('map'), {
        center: {
            lat: 38.6270,
            lng: -90.1994
        },
        zoom: 15
    });
    for (var i = 0; i < place_ids.length; i++) {
        console.log('hi');
        console.log(place_ids[i]);
        var infowindow = new google.maps.InfoWindow();
        var service = new google.maps.places.PlacesService(map);

        service.getDetails({
            placeId: place_ids[i] // grab placeids from multiple shelters and create markers / id
        }, function(place, status) {
            if (status === google.maps.places.PlacesServiceStatus.OK) {
                var image = 'http://findicons.com/files/icons/1150/tango/32/go_home.png'
                var marker = new google.maps.Marker({
                    map: map,
                    position: place.geometry.location,
                    icon: image
                });
                google.maps.event.addListener(marker, 'click', function() {
                    infowindow.setContent('<div><strong>' + place.name + '</strong><br>' +
                        'Place ID: ' + place.place_id + '<br>' +
                        place.formatted_address + '</div>');
                    infowindow.open(map, this);
                });
            }
        });
    }
}
