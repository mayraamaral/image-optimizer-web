from django.urls import path
from . import views
from .download_and_delete_image_view import download_image

urlpatterns = [
    path('', views.index, name='index'),
    path('download/<str:filename>/', download_image, name='download_image')
]
