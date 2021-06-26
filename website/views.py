from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DeleteView, FormView
from .models import *
from django.urls import reverse_lazy
from .forms import *
# Create your views here.


class IndexView(TemplateView):
    template_name = 'website/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['company'] = Company.objects.get(id=1)
        return context


class WorksView(ListView):
    template_name = 'website/works.html'
    model = Work
    paginate_by = 9

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['works_length'] = len(self.object_list)
        return context


class WorkDetailView(DeleteView):
    template_name = 'website/work_detail.html'
    model = Work


class CraftsView(ListView):
    template_name = 'website/crafts.html'
    model = Craft
    paginate_by = 9

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['crafts_length'] = len(self.object_list)
        return context


class CraftDetailView(DeleteView):
    template_name = 'website/craft_detail.html'
    model = Craft


class ContactView(FormView):
    template_name = 'website/contact.html'
    success_url = reverse_lazy('website:index')
    form_class = ContactForm