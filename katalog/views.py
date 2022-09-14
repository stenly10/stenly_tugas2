from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.
def show_katalog(request):
    data_barang_katalog = CatalogItem.objects.all()
    context = {
        'nama': 'Stenly Yosua Saputra',
        'id': '2106704244',
        'list_barang': data_barang_katalog
    }
    return render(request, "katalog.html", context)