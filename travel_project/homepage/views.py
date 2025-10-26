from django.shortcuts import render
from places.models import Place
import json


def index(request):
    places = Place.objects.all()

    features = []
    for place in places:
        features.append({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.lng, place.lat]
            },
            "properties": {
                "title": place.title,
                "placeId": place.id,
                "detailsUrl": f"/places/{place.id}/"
            }
        })

    geojson = {
        "type": "FeatureCollection",
        "features": features
    }

    context = {
        'places_geojson': json.dumps(geojson)
    }

    return render(request, 'homepage/index.html', context)
