from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from .models import Phone
from .serializers import PhoneSerializer
from rest_framework import viewsets


class PhoneViewSet(viewsets.ModelViewSet):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer

def index(request):
    template = loader.get_template('xiaomi/index.html')    
    return HttpResponse(template.render({}, request))
    
def return_json(request):
    phones = Phone.objects.all().values('title', 'price', 'link')
    phones_list = list(phones)
    return JsonResponse(phones_list, safe = False)
    
def doc(request):
    context = '1. Install requirements from requirements.txt\n'
    context += '2. Start spider from "apl_spyder/crawl.py"\n'
    context += '3. Check JSON API or simple JSON result from the links below"\n'
    template = loader.get_template('xiaomi/doc.html')
    return HttpResponse(template.render({'context' : context}, request))