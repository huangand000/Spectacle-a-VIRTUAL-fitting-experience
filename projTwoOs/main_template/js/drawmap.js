var map;
var infowindow;
var userCoord = null;
var directionsService;
var directionsDisplay;
var markerCoord;
var storeID;
var service;
function initMap() {
    var styledMapType = new google.maps.StyledMapType(
      [
        {
            "elementType": "geometry",
            "stylers": [
            {
                "color": "#242f3e"
            }
            ]
        },
        {
            "elementType": "labels.text.fill",
            "stylers": [
            {
                "color": "#746855"
            }
            ]
        },
        {
            "elementType": "labels.text.stroke",
            "stylers": [
            {
                "color": "#242f3e"
            }
            ]
        },
        {
            "featureType": "administrative",
            "elementType": "geometry",
            "stylers": [
            {
                "visibility": "off"
            }
            ]
        },
        {
            "featureType": "administrative.locality",
            "elementType": "labels.text.fill",
            "stylers": [
            {
                "color": "#d59563"
            }
            ]
        },
        {
            "featureType": "poi",
            "stylers": [
            {
                "visibility": "off"
            }
            ]
        },
        {
            "featureType": "poi",
            "elementType": "labels.text.fill",
            "stylers": [
            {
                "color": "#d59563"
            }
            ]
        },
        {
            "featureType": "poi.park",
            "elementType": "geometry",
            "stylers": [
            {
                "color": "#263c3f"
            }
            ]
        },
        {
            "featureType": "poi.park",
            "elementType": "labels.text.fill",
            "stylers": [
            {
                "color": "#6b9a76"
            }
            ]
        },
        {
            "featureType": "road",
            "elementType": "geometry",
            "stylers": [
            {
                "color": "#38414e"
            }
            ]
        },
        {
            "featureType": "road",
            "elementType": "geometry.stroke",
            "stylers": [
            {
                "color": "#212a37"
            }
            ]
        },
        {
            "featureType": "road",
            "elementType": "labels.icon",
            "stylers": [
            {
                "visibility": "off"
            }
            ]
        },
        {
            "featureType": "road",
            "elementType": "labels.text.fill",
            "stylers": [
            {
                "color": "#9ca5b3"
            }
            ]
        },
        {
            "featureType": "road.highway",
            "elementType": "geometry",
            "stylers": [
            {
                "color": "#746855"
            }
            ]
        },
        {
            "featureType": "road.highway",
            "elementType": "geometry.stroke",
            "stylers": [
            {
                "color": "#1f2835"
            }
            ]
        },
        {
            "featureType": "road.highway",
            "elementType": "labels.text.fill",
            "stylers": [
            {
                "color": "#f3d19c"
            }
            ]
        },
        {
            "featureType": "transit",
            "stylers": [
            {
                "visibility": "off"
            }
            ]
        },
        {
            "featureType": "transit",
            "elementType": "geometry",
            "stylers": [
            {
                "color": "#2f3948"
            }
            ]
        },
        {
            "featureType": "transit.station",
            "elementType": "labels.text.fill",
            "stylers": [
            {
                "color": "#d59563"
            }
            ]
        },
        {
            "featureType": "water",
            "elementType": "geometry",
            "stylers": [
            {
                "color": "#17263c"
            }
            ]
        },
        {
            "featureType": "water",
            "elementType": "labels.text.fill",
            "stylers": [
            {
                "color": "#515c6d"
            }
            ]
        },
        {
            "featureType": "water",
            "elementType": "labels.text.stroke",
            "stylers": [
            {
                "color": "#17263c"
            }
            ]
        }
        ],
    {name: 'Styled Map'});

    var pos = {lat: 47.4505, lng: -122.2519}; //southcenter coordinates
    
    directionsDisplay = new google.maps.DirectionsRenderer;
    directionsService = new google.maps.DirectionsService;
    map = new google.maps.Map(document.getElementById('map'), {
    center: pos,
    zoom: 15
    });
    infoWindow = new google.maps.InfoWindow();
    getMarkers();

    map.addListener('center_changed', function() {
        getMarkers();
    });
    directionsDisplay.setMap(map);

    // Get HTML5 geolocation.
    if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function(position) {
        userCoord = {
        lat: position.coords.latitude,
        lng: position.coords.longitude
        };

        infoWindow.setPosition(userCoord);
        infoWindow.setContent('Location found.');
        infoWindow.open(map);
        map.setCenter(userCoord);
        map.setZoom(15)
    }, function() {
        handleLocationError(true, infoWindow, map.getCenter());
        findStores();
        });
    } else {
        // Browser doesn't support Geolocation
        handleLocationError(false, infoWindow, map.getCenter());
    }
    map.mapTypes.set('styled_map', styledMapType);
    map.setMapTypeId('styled_map');
}

function getMarkers(){
    service = new google.maps.places.PlacesService(map);
    service.nearbySearch({
    location: map.getCenter(),
    radius: 5000,
    type: ['store'],
    keyword: 'glasses'
    }, callback);
}

function callback(results, status) {
    if (status === google.maps.places.PlacesServiceStatus.OK) {
        for (var i = 0; i < results.length; i++) {
            createMarker(results[i]);
        }
    }
}

function createMarker(place) {
    var placeLoc = place.geometry.location;
    var marker = new google.maps.Marker({
        map: map,
        position: place.geometry.location
    });

    google.maps.event.addListener(marker, 'click', function() {
        markerCoord = {lat: marker.getPosition().lat(), lng: marker.getPosition().lng()}
        storeID = place.place_id
        infoWindow.setContent("<h3>" + place.name + "</h3> <p onclick='getStoreInfo()'>Click for more info! </p>");
        infoWindow.open(map, this);
        directionsDisplay.setMap(map);
        directionsDisplay.setPanel(document.getElementById('right-panel'));
    });
}

function getStoreInfo(){
    service = new google.maps.places.PlacesService(map);
    service.getDetails({
        placeId: storeID
    }, function(place, status) {
        if (status == google.maps.places.PlacesServiceStatus.OK) {
            $('#store-info').html('');
            $('#store-info').append("<h3>Place name: " + place.name + "</h3>");
            $('#store-info').append("<h4>Ratings: " + place.rating +"</h4>");
            $('#store-info').append("<p> Address: " + place.formatted_address + ' <h4 id="address" onclick="calculateAndDisplayRoute()">(Click for directions)</h4></p>');
            $('#store-info').append("<h4>Hours:</h4>");
            for (var time in place.opening_hours.weekday_text) {
                $('#store-info').append('<p>' +place.opening_hours.weekday_text[time] +'</p>');
            }
        }
    }); 
}
function calculateAndDisplayRoute() {
    if (userCoord) { //if user provides geolocation
        directionsService.route({
            origin: userCoord, //user coordinates
            destination: markerCoord, 
            travelMode: 'DRIVING'
        }, function(response, status) {
            if (status == 'OK') {
                directionsDisplay.setDirections(response);
            } else {
                window.alert('Directions request failed due to ' + status);
            }
        });
    } else {
        window.alert('User must share location to locate store');
    }
}
