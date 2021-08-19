from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView
from django.contrib.messages.views import SuccessMessageMixin
from .models import *
from django.urls import reverse
from .forms import *
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
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

    def get_queryset(self):
        q_category = self.request.GET.get('q')
        print(q_category)
        if not q_category:
            object_list = Work.objects.all()
        else:
            object_list = Work.objects.filter(category=q_category)
            print(object_list)
        return object_list


class WorkDetailView(DetailView):
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


class CraftDetailView(DetailView):
    template_name = 'website/work_detail.html'
    model = Craft


class ContactView(CreateView, SuccessMessageMixin):
    template_name = 'website/contact.html'
    model = Contact
    fields = ['name', 'send_by', 'tel', 'content']

    def get_success_url(self):
        return reverse('index')