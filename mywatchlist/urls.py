# TODO: Implement Routings Here
from django.urls import path
from mywatchlist.views import show_watchlist
from mywatchlist.views import show_html
from mywatchlist.views import show_json
from mywatchlist.views import show_xml


app_name = 'mywatchlist'

urlpatterns = [
    path('', show_watchlist, name='show_watchlist'),
    path('json/', show_json, name='show_json'),
    path('xml/', show_xml, name='show_xml')
]