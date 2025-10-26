from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Place


def place_detail(request, place_id):
    place = get_object_or_404(Place, id=place_id)
    images = [img.image.url for img in place.images.all()]
    data = {
        "title": place.title,
        "imgs": images,
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lng": place.lng,
            "lat": place.lat
        }
    }
    return JsonResponse(data, json_dumps_params={'ensure_ascii': False, 'indent': 2})