var goodAnsRange = settings.goodAnsRange; //How far an answer can be and still be corrected
var totallyWrong = settings.totallyWrong; // How far an answer can be before it is considered totally wrong

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




function initializeAnswer(correctAnswer, answer, givenAnswer) {
    $('.answer-container').append('<div id="map" ></div>');
    var map = new google.maps.Map(document.getElementById('map'), {
          zoom: 7,
         center: { lat: 52.059042,
          lng: 5.470902 },
           mapTypeId: 'terrain'
    });

    initializePolygons(nlPoly, map);


    showAnswer(correctAnswer, answer, givenAnswer, map);


}

function drawLine(coor1, coor2, map) {

    lineColor= (settings.ansLineColor ===undefined) ? "#FF0000" : settings.ansLineColor;
    opacity= (settings.ansStrokeOpacity ===undefined) ? 1.0 : settings.ansStrokeOpacity;
    weight= (settings.ansStrokeWeight ===undefined) ? 2 : settings.ansStrokeWeight;

    var flightPath = new google.maps.Polyline({
        path: [coor1, coor2],
        geodesic: true,
        strokeColor: lineColor,
        strokeOpacity: opacity,
        strokeWeight: weight
    });

    flightPath.setMap(map);
}

function drawMarkers(correctAnswer, givenAnswer, map) {
    drawMarker(correctAnswer, "Correct answer", map, settings.correctAnswerColor);
    drawMarker(givenAnswer, "Your answer", map, settings.yourAnswerColor);
}


function drawMarker(coord, message, map, color) {
    var marker = new google.maps.Marker({
        position: coord,
        icon: `https://maps.google.com/mapfiles/ms/icons/${color}-dot.png`,
        map: map,
        title: message
    });
    var infowindow = new google.maps.InfoWindow({
        content: message,
    });

    google.maps.event.addListener(marker, 'mouseover', function () {
        infowindow.open(map, this);
    });
    google.maps.event.addListener(marker, 'mouseout', function () {
        infowindow.close();
    });
}

/**
 * Shows the answers to the user.
 * @param correctAnswer
 * @param answer
 * @param givenAnswer
 */
function showAnswer(correctAnswer, answer, givenAnswer, map) {
    var difference = Math.round(distanceInKmBetweenEarthCoordinates(correctAnswer.lat, correctAnswer.lng, givenAnswer.lat, givenAnswer.lng));

    if(difference < goodAnsRange){

         $('.answer-container').prepend(`<p>Dat klopt, het juiste antwoord is ${answer}.</p>`)
         drawMarker(givenAnswer, "Correct answer", map, settings.correctAnswerColor);
    } else {
        drawMarkers(correctAnswer, givenAnswer, map);
        drawLine(correctAnswer, givenAnswer, map);
        $('.answer-container').prepend(`<p>Het juiste antwoord was ${answer}.</p>
        <p>Het verschil is ${difference} km.</p>`);
    }


}

function degreesToRadians(degrees) {
    return degrees * Math.PI / 180;
}

function distanceInKmBetweenEarthCoordinates(lat1, lon1, lat2, lon2) {
    var earthRadiusKm = 6371;

    var dLat = degreesToRadians(lat2 - lat1);
    var dLon = degreesToRadians(lon2 - lon1);

    lat1 = degreesToRadians(lat1);
    lat2 = degreesToRadians(lat2);

    var a = Math.sin(dLat / 2) * Math.sin(dLat / 2) +
        Math.sin(dLon / 2) * Math.sin(dLon / 2) * Math.cos(lat1) * Math.cos(lat2);
    var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
    return earthRadiusKm * c;
}

function distanceBetweenAns(ans1, ans2){
    return distanceInKmBetweenEarthCoordinates(ans1["lat"], ans1["lng"], ans2["lat"],ans2["lng"])
}