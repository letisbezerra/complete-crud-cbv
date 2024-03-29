#from django.shortcuts import render 
#from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from .models import Cliente

class ClienteCreate(CreateView):
    model = Cliente
    fields = '__all__'
    success_url = reverse_lazy('core:list')  

class ClienteList(ListView):
    model = Cliente 
    queryset = Cliente.objects.all() 

class ClienteUpdate(UpdateView):
    model = Cliente
    fields = '__all__'
    success_url = reverse_lazy('core:list')

class ClienteDetail(DetailView): 
    queryset = Cliente.objects.all()


class ClienteDelete(DeleteView):
    model = Cliente
    queryset = Cliente.objects.all()
    success_url = reverse_lazy('core:list')