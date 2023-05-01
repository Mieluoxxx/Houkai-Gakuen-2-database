from django.shortcuts import render
from django.http import HttpResponse
from common.models import Customer


# Create your views here.
def listcostumers(request):
    qs = Customer.objects.values()

    restr = ''
    for costumer in qs:
        for name, value in costumer.items():
            restr += f'{name}: {value} |'

        restr += '<br>'

    return HttpResponse(restr)
