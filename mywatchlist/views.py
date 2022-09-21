from django.shortcuts import render
from mywatchlist.models import MyWatchList
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_watchlist(request):
    watch_list = MyWatchList.objects.all()
    context = {
        'nama': 'Stenly Yosua Saputra',
        'id': '2106704244',
        'watch_list': watch_list
    }
    return render(request, "mywatchlist.html", context)

def show_json(request):
    watch_list = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", watch_list), content_type="application/json")

def show_xml(request):
    watch_list = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", watch_list), content_type="application/xml")
