from django.urls import path
from .views import image_upload_view, image_list_view

app_name = 'gallery'

urlpatterns = [
    path('upload/', image_upload_view, name='image_upload'),
    path('', image_list_view, name='image_list'),
]
