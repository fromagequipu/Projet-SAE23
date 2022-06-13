# Create your views here.

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from computerApp.models import Machine
from computerApp.models import Serveur
from computerApp.models import Routeur
from computerApp.models import Switch
#from computermngt.computerApp.forms import AddMachineForm
from .forms import AddMachineForm



def index(request) :
    machines = Machine.objects.all()
    serveur = Serveur.objects.all()
    routeur = Routeur.objects.all()
    switch =Switch.objects.all()
    context = {'serveur': serveur,'machines': machines, 'routeur': routeur, 'switch': switch
    }
    return render(request, 'index.html', context)

#def index1(request) :
    #serveur = Serveur.objects.all()
    #context = {'serveur': serveur,
    #}
    #return render(request, 'index.html', context)


    
def machine_list_view(request) :
    machines = Machine.objects.all()
    context={'machines': machines}
    return render(request,
     'computerapp/index.html',
     context)

def machine_detail_view(request, pk):
    machine = get_object_or_404(Machine, id=pk)
    context={'machine':machine}
    return render(request, 
     'computerapp/machine_detail.html',
     context)
     
def machine_add_form(request):
    if request.method == 'POST':
        form = AddMachineForm(request.POST or None)
        if form.is_valid():
            new_machine = Machine(nom=form.cleaned_data['nom'])
            new_machine.save()
            return redirect('machines')
    else:
        form = AddMachineForm()
        context = {'form': form}
        return render(request,
        'computerapp/machine_add.html',context)


def b(request):
    context = {}
    return render(request, 'b.html',context)

def d(request):
    routeur = Routeur.objects.all()
    switch =Switch.objects.all()
    context = {'routeur': routeur, 'switch': switch}
    return render(request, 'd.html', context)

def e(request):
    machines = Machine.objects.all()
    serveur = Serveur.objects.all()
    context = {'serveur': serveur,'machines': machines}
    return render(request, 'e.html', context)

def contact(request):
    context = {}
    return render(request, 'contact.html', context)