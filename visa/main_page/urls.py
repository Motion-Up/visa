from django.urls import path
from . import views


app_name = 'main_page'


urlpatterns = [
    path('', views.index, name='index'),
    path('sitemap.xml', views.site_map, name='site_map'),
]