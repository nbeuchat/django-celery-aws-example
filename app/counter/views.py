from django.shortcuts import render
from django.http import HttpResponse
from .tasks import add_analytics

# Create your views here.
def index(request):
    output = 'Test'
    ua = request.META['HTTP_USER_AGENT']
    print(ua)
    #add_analytics.delay(ua)
    print(add_analytics.name)
    res = add_analytics.delay(ua)
    res.get()
    print('delay done')
    return HttpResponse(output)