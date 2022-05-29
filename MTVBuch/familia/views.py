from django.shortcuts import render
from familia.models import Familiar


# Create your views here.
def familiares(request):
    integrante_1 = Familiar.objects.create(
            nombre = 'Alejandro',
            edad = 67,
            nacimiento = '1955-2-7',
            parentezco = 'padre'
            )
    integrante_2 = Familiar.objects.create(
            nombre = 'Griselda',
            edad = 66,
            nacimiento = '1956-3-5',
            parentezco = 'madre'
            )
    integrante_3 = Familiar.objects.create(
            nombre = 'Eric',
            edad = 35,
            nacimiento = '1986-11-9',
            parentezco = 'hermano'
            )
    
    context = {'integrante_1':integrante_1, 'integrante_2':integrante_2, 'integrante_3':integrante_3}
    return render(request, 'familiares.html', context=context)