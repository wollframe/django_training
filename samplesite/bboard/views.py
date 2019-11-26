from django.shortcuts import render
from django.template import loader
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.http import HttpResponse
from . import forms

from .forms import BbForm, Cl
from .models import *

def index(request):
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    form = forms.Cl()
    context = {
        'bbs': bbs,
        'rubrics': rubrics,
        'form': form,
        }
    if request.method == "POST":
        form = forms.Cl(request.POST)
        if form.is_valid():
            print("Result")
            ml = (form.cleaned_data['km'])
            result = ml*16+150

            return render (request, 'bboard/index.html', {'result': result})

    return render (request, 'bboard/index.html', context)

def by_rubric(request, rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)


    context = {
        'bbs': bbs,
        'rubrics': rubrics,
        'current_rubric': current_rubric,
    }
    return render (request, 'bboard/by_rubric.html', context)

def detail(request, bb_id):
    a = Bb.objects.get(pk = bb_id)
    context = {
        'detail' : a,
    }
    return render(request, 'bboard/detail.html', context)


class BbCreateView(CreateView):
    template_name = 'bboard/create.html'
    form_class = BbForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        
        return context
