from django.shortcuts import render
from .models import BettingOdds, PinnacleHighlight

# Create your views here.
def tableview(request):
    leaguelist = BettingOdds.objects.order_by('leagueid')
    context = {'league_list': leaguelist}
    return render(request, "table/tablehtml.html", context)

def homepage(request):
    return render(request, "index.html")

def pinnacleview(request):
    pinlist = PinnacleHighlight.objects.order_by('id')
    context = {'pinlist': pinlist}
    return render(request, "table/pinnacleview.html", context)