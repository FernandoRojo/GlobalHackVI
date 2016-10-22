
var map, heatmap;

function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        zoom: 13,
        center: {lat: 38.620142, lng: -90.188515},
        mapTypeId: 'satellite'
    });

    heatmap = new google.maps.visualization.HeatmapLayer({
        data: getPoints(),
        map: map
    });
}

function toggleHeatmap() {
    heatmap.setMap(heatmap.getMap() ? null : map);
}


function changeGradient() {
    var gradient = [
        'rgba(0, 255, 255, 0)',
        'rgba(0, 255, 255, 1)',
        'rgba(0, 191, 255, 1)',
        'rgba(0, 127, 255, 1)',
        'rgba(0, 63, 255, 1)',
        'rgba(0, 0, 255, 1)',
        'rgba(0, 0, 223, 1)',
        'rgba(0, 0, 191, 1)',
        'rgba(0, 0, 159, 1)',
        'rgba(0, 0, 127, 1)',
        'rgba(63, 0, 91, 1)',
        'rgba(127, 0, 63, 1)',
        'rgba(191, 0, 31, 1)',
        'rgba(255, 0, 0, 1)'
    ]
  heatmap.set('gradient', heatmap.get('gradient') ? null : gradient);
}

function changeRadius() {
    heatmap.set('radius', heatmap.get('radius') ? null : 20);
}

function changeOpacity() {
    heatmap.set('opacity', heatmap.get('opacity') ? null : 0.2);
}

// Heatmap data: 500 Points
function Get(yourUrl){
    var Httpreq = new XMLHttpRequest(); // a new request
    Httpreq.open('GET',yourUrl,false);
    Httpreq.send(null);
    return Httpreq.responseText;          
}


function getPoints() {
    var json_obj = Get('/shelters/heatdata');
    json_obj = JSON.parse(json_obj);
    json_obj = JSON.parse(json_obj);
    points = [];
    for (var i in json_obj){
	lat = json_obj[i]["fields"]['latitude'];
	lng = json_obj[i]["fields"]["longitude"];
	points.push(new google.maps.LatLng(lat,lng));
    }
    return points;

    
}
    <script async defer
src="https://maps.googleapis.com/maps/api/js?key=AIzaSyDIT5WqChLN0yTAnQNB0r5CN-shZrAtxbM&libraries=visualization&callback=initMap">
    </script>
  
