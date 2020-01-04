$(document).ready(function(){
    var Core;
    !function(a){

    }(Core || (Core = {}));

    var Geo;
    !function(a){
        var b = function (){
            if(navigator.geolocation){
                navigator.geolocation.getCurrentPosition(a.getLocation);
            }else{
                console.log("Geo-location not available");
            }
        };
        var c = function(b){
            $('input[name=latitude]').val(b.coords.latitude);
            $('input[name=longitude]').val(b.coords.longitude);

        };
        a.checkLocation = b, a.getLocation = c;
    }(Geo || (Geo = {}));
    Geo.checkLocation();
});