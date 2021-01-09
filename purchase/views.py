from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def purchase_entry(request):
    return render(request, 'purchase_entry.html')
