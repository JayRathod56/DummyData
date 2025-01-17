from django.urls import path
from .views import TestJsonRead

urlpatterns = [
    path('', TestJsonRead.as_view(), name='stream_json'),
]