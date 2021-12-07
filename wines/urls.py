from django.urls import path
from rest_framework import urlpatterns
from . import views
from .views import WineViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'', WineViewSet, basename="wines")
urlpatterns = router.urls

# urlpatterns = [
#     path('', views.wine_list, name='wine_list'),
#     path('new', views.new_wine, name='new_wine'),
#     path('<int:wine_id>', views.wine_detail, name='wine_detail'),
#     path('<int:wine_id>/edit', views.edit_wine, name='edit_wine'),
#     path('<int:wine_id>/delete', views.delete_wine, name='delete_wine'),
# ]
