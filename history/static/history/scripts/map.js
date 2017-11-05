
function initMap() {
        var map = new google.maps.Map(document.getElementById('map'), {
          zoom: 8,
          center: {lat: -34.397, lng: 150.644}
        });
        var geocoder = new google.maps.Geocoder();

        document.getElementById('submit').addEventListener('click', function() {
          geocodeAddress(geocoder, map);
        });
        alert("why");
        document.getElementById('submit').addEventListener('keypress', function(event) {
          event.preventDefault();
          if(event.keyCode === 13){
            geocodeAddress(geocoder, map);
            //document.getElementById("id_of_button").click();
          }
          });
      }

      function geocodeAddress(geocoder, resultsMap) {
        var address = document.getElementById('address').value;
        geocoder.geocode({'address': address}, function(results, status) {
          if (status === 'OK') {
            var loc = results[0].geometry.location;
            resultsMap.setCenter();
            var marker = new google.maps.Marker({map: resultsMap, position: loc});
            alert(loc.lat());
            window.location.href="/worst/" + loc.lat() + "/" + loc.lng();
          } 
          else {
            alert('Geocode was not successful for the following reason: ' + status);
          }
        });
      }
