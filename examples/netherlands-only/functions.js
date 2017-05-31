function initializePolygons(provincies, map) {
    var polygons = [];
    for (prov in provincies) {
        for (i in provincies[prov]) {
            var paths = provincies[prov][i].map(obj => {
                return {lat: parseFloat(obj.lat), lng: parseFloat(obj.lng)};
            });
            var poly = new google.maps.Polygon({
                paths: paths,
                strokeColor: '#FF0000',
                strokeOpacity: 0,
                strokeWeight: 2,
                fillColor: '#FF0000',
                fillOpacity: 0.35
            });

            poly.setMap(map);
            polygons.push(poly);

        }


    }
    return polygons;
}

function isInside(polygons, coordinates) {
    for (i in polygons) {
        var poly = polygons[i];
        if (google.maps.geometry.poly.containsLocation(coordinates, poly)) {
            return true;
        }

    }
    return false;
}

function addEvents(polygons, map) {
    var marker;
    for (i in polygons) {
        var poly = polygons[i];
        poly.addListener('click', (event) => {
            lat = event.latLng.lat();
            lng = event.latLng.lng();
            if (!marker) {
                marker = new google.maps.Marker({
                    position: {lat: lat, lng: lng},
                    map: map,
                    title: 'Your answer!',
                    draggable: true
                });

                marker.addListener("dragend", (e) => {
                    if (!isInside(polygons, e.latLng)) {
                        marker.setMap(null);
                        marker = null;
                    }
                })
            } else {
                var latlng = new google.maps.LatLng(lat, lng);
                marker.setPosition(latlng);
            }
        })
    }

}



