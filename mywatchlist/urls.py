# TODO: Implement Routings Here
from django.urls import path
from mywatchlist.views import show_json
from mywatchlist.views import show_xml
from mywatchlist.views import show_html


app_name = 'mywatchlist'

urlpatterns = [
    path('json/', show_json, name='show_json'),
    path('xml/', show_xml, name='show_xml'),
    path('html/', show_html, name='show_html')
]