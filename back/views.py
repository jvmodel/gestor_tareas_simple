from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import NuevaTareaForm, BorrarTareaForm
from .models import Tarea

class Tareas(ListView):
    model = Tarea
    template_name = 'back/start.html'
    context_object_name = 'tareas'
    extra_context = {'title': 'Mis Tareas'}


class Nuevo(CreateView):
    model = Tarea
    form_class = NuevaTareaForm
    template_name = 'back/nuevo.html'
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class Ver(UpdateView):
    model = Tarea
    form_class = NuevaTareaForm
    template_name = 'back/nuevo.html'
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class Borrar(DeleteView):
    model = Tarea
    form_class = BorrarTareaForm
    template_name = 'back/nuevo.html'
    success_url = '/'
    extra_context = {'title': 'Completada?',
                     'message': 'Marcar como completado y eliminar'}
