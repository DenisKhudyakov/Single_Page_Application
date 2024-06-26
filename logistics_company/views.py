from django.shortcuts import render
from django.views.generic import ListView

from logistics_company.models import Registry


class MainTableListView(ListView):
    template_name = 'logistics_company/main.html'
    model = Registry

    def get_queryset(self):
        return Registry.objects.all()

