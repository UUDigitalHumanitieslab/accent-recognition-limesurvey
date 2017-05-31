function initializeAnswer(correctAnswer, answer, givenAnswer) {
    $('.answer-container').append('<div id="map" ></div>');
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 7,
        center: correctAnswer
    });

    drawMarkers(correctAnswer, givenAnswer, map);
    drawLine(correctAnswer, givenAnswer, map);
    showAnswer(correctAnswer, answer, givenAnswer);

}

function drawLine(coor1, coor2, map) {
    var flightPath = new google.maps.Polyline({
        path: [coor1, coor2],
        geodesic: true,
        strokeColor: settings.lineColor,
        strokeOpacity: 1.0,
        strokeWeight: 2
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
        icon: `http://maps.google.com/mapfiles/ms/icons/${color}-dot.png`,
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

function showAnswer(correctAnswer, answer, givenAnswer) {
    var difference = Math.round(distanceInKmBetweenEarthCoordinates(correctAnswer.lat, correctAnswer.lng, givenAnswer.lat, givenAnswer.lng));
    $('.answer-container').prepend(`<p>Het juiste antwoord: ${answer}</p>
        <p>Het verschil: ${difference} km</p>`);
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
