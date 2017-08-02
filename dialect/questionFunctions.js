function initializePolygons(provincies, map) {
    var polygons = [];
    for (prov in provincies) {
        for (i in provincies[prov]) {
            var paths = provincies[prov][i].map(obj => {
                return {lat: parseFloat(obj.lat), lng: parseFloat(obj.lng)};
            });
            var poly = new google.maps.Polygon({
                paths: paths,
                strokeColor: settings.strokeColor,
                strokeOpacity: settings.strokeOpacity,
                strokeWeight: settings.strokeWeight,
                fillColor: settings.mapColor,
                fillOpacity: settings.opacity
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

                setAnswer(lat, lng)

                marker.addListener("dragend", (e) => {
                    if (!isInside(polygons, e.latLng)) {
                        marker.setMap(null);
                        marker = null;
                        emptyAnswer();
                    } else {
                        setAnswer(e.latLng.lat(), e.latLng.lng());
                    }
                })
            } else {
                var latlng = new google.maps.LatLng(lat, lng);
                marker.setPosition(latlng);
                setAnswer(lat, lng)
            }
        })
    }

}

function setAnswer(lat, lng){
    $('.textarea').val(`{ "lat": ${lat}, "lng":${lng} }`);
}

function emptyAnswer(){
    $('.textarea').val("");
}


function initializeQuestion(audioRef, autoplay){
    console.log("initialize question")
    $(document).ready(function(){
        var answerContainer = $('.answer-container')
        answerContainer.append('<div id="map" >This is some text</div>')
        answerContainer.prepend(
            `<h3>Audio</h3> <audio controls ${autoplay?"autoPlay":""}> <source src=${audioRef} type="audio/ogg"> </audio>`)
        var map = new google.maps.Map(document.getElementById('map'), {
            zoom: 7,
            center: { lat: 52.059042,
                lng: 5.470902 },
            mapTypeId: 'terrain'
        });


        var polygons = initializePolygons(nlPoly, map);
        addEvents(polygons, map);
        var warningtxt = $("#bootstrap-alert-box-modal .modal-body>p")
        console.log(warningtxt)
        warningtxt.text("Warning no marker placed.");



    })


}



