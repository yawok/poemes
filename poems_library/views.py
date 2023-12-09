from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import  ListView, DetailView, CreateView, UpdateView, DeleteView
from . import models, forms

class PoemsListView(ListView):
    queryset = models.Poem.objects.all()
    context_object_name = "poems"
    template_name = "poems_library/poems_list.html"
    

class PoemDetailView(DetailView):
    template_name = "poems_library/poem.html"
    model = models.Poem
    

class PoemCreateView(CreateView):
    form_class = forms.PoemForm
    template_name = "poems_library/create.html"
    
    def get_success_url(self) -> str:
        return reverse_lazy("poems_list")
    
    
class PoemUpdateView(UpdateView):
    model = models.Poem
    context_object_name = "poem"
    form_class = forms.PoemForm
    template_name = "poems_library/update.html"
    success_url = reverse_lazy("poems_list")
    

class PoemDeleteView(DeleteView):
    model = models.Poem
    context_object_name = "poem"
    template_name = "poems_library/delete.html"
    success_url = reverse_lazy("poems_list")