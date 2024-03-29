# Create your views here.

#from django.http import JsonResponse
#from django.views.decorators.csrf import csrf_exempt
#from .forms import WineForm
from .models import Wine
from .serializers import WineSerializer
from rest_framework import viewsets
#import json

class WineViewSet(viewsets.ModelViewSet):
    queryset = Wine.objects.all()
    serializer_class = WineSerializer


# def wine_list(request):
#     wines = Wine.objects.all()
#     serialized_wines = WineSerializer(wines).all_wines
#     return JsonResponse(data=serialized_wines, status=200)


# def wine_detail(request, wine_id):
#     wine = Wine.objects.get(id=wine_id)
#     serialized_wine = WineSerializer(wine).wine_detail
#     return JsonResponse(data=serialized_wine, status=200)


# @csrf_exempt
# def new_wine(request):
#     if request.method == "POST":
#         data = json.load(request)
#         form = WineForm(data)
#         if form.is_valid():
#             wine = form.save(commit=True)
#             serialized_wine = WineSerializer(wine).wine_detail
#             return JsonResponse(data=serialized_wine, status=200)


# @csrf_exempt
# def edit_wine(request, wine_id):
#     wine = Wine.objects.get(id=wine_id)
#     if request.method == "POST":
#         data = json.load(request)
#         form = WineForm(data, instance=wine)
#         if form.is_valid():
#             wine = form.save(commit=True)
#             serialized_wine = WineSerializer(wine).wine_detail
#             return JsonResponse(data=serialized_wine, status=200)


# @csrf_exempt
# def delete_wine(request, wine_id):
#     if request.method == "POST":
#         wine = Wine.objects.get(id=wine_id)
#         wine.delete()
#     return JsonResponse(data={'status': 'Successfully deleted wine.'}, status=200)
