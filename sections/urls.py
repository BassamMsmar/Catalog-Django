from django.urls import path

from .views import sections_list


urlpatterns = [
    path('', sections_list, name='sections_list')
]
