from django.http import HttpResponse
from django.template import Template, Context

def saludo(request):
    return HttpResponse('Bienvenidos al proyecto Primer MVT')


