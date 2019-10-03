from django.utils import timezone
from django.views.generic.list import ListView
from django.shortcuts import render
from rest_framework import viewsets
from . import serializers
from . import models
from . import forms


def home(request):
    return render(request, template_name='basic/home.html')

class FirstView(viewsets.ModelViewSet):
    queryset = models.First.objects.all()
    serializer_class = serializers.FirstSerializer


class SecondView(viewsets.ModelViewSet):
    queryset = models.Second.objects.all()
    serializer_class = serializers.SecondSerializer


class FirstListView(ListView):
    model = models.First
    template_name = 'basic/firstlist.html'
    ordering = ['-id']

    def get_context_data(self, **kwargs):
        print("METHOD: ", self.request.GET)
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['filter_form'] = forms.FirstListForm()
        return context

    def get_queryset(self, **kwargs):
        form_type = self.request.GET.get('form_type', '')
        print(form_type)
        queryset = models.First.objects.all()
        if form_type:
            queryset = queryset.filter(form_type = form_type)
        return queryset


