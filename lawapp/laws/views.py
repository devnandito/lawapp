# coding=utf-8

# Django
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, InvalidPage, EmptyPage

# Models
from lawapp.laws.models import Law

# Forms
from lawapp.laws.forms import LawForm


# Utilities
from lawapp.utils.functions import get_url, get_body, get_button

def get_name():
    name = ['Leyes', 'leyes', 'Ley', 'ley']
    return name

@login_required()
def show_law(request):
    tmp = get_name()
    list_title = ['#', 'Titulo', 'Acciones']
    template = loader.get_template('laws/show.html')
    list_paginator = Law.objects.all()
    paginator = Paginator(list_paginator, 10)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        object_list = paginator.page(page)
    except (EmptyPage, InvalidPage):
        object_list = paginator.page(paginator.num_pages)
    context = {
        'title': get_body(tmp[3], tmp[0]),
        'object_list': object_list,
        'uri': get_url('laws'),
        'list_title': list_title,
    }
    return HttpResponse(template.render(context, request))

@login_required()
def create_law(request):
    tmp = get_name()
    button = get_button()
    template = loader.get_template('laws/add.html')
    if request.method == 'POST':
        form = LawForm(request.POST)
        if form.is_valid():
            form.save()
            message = 'Los datos se guardaron correctamente!'
            tpl = loader.get_template('messages/message.html')
            contextSuccess = {
                'title': get_body(tmp[3], tmp[0]),
                'uri': get_url('laws'),
                'message': message,
            }
            return HttpResponse(tpl.render(contextSuccess, request))
    else:
        form = LawForm()
    context = {
        'title': get_body(tmp[3], tmp[0]),
        'form': form,
        'uri': get_url('laws'),
        'button': button[1],
    }
    return HttpResponse(template.render(context, request))

@login_required()
def edit_law(request, pk):
    tmp = get_name()
    button = get_button()
    template = loader.get_template('laws/edit.html')
    ins = get_object_or_404(Law, pk=pk)
    if request.method == 'POST':
        form = LawForm(request.POST, instance=ins)
        if form.is_valid():
            form.save()
            message = 'Los datos se guardaron correctamente!'
            tpl = loader.get_template('messages/message.html')
            contextSuccess = {
                'title': get_body(tmp[3], tmp[0]),
                'uri': get_url('laws'),
                'message': message,
            }
            return HttpResponse(tpl.render(contextSuccess, request))
    else:
        form = LawForm(instance=ins)
    context = {
        'title': get_body(tmp[3], tmp[0]),
        'form': form,
        'uri': get_url('laws'),
        'button': button[1],
    }
    return HttpResponse(template.render(context, request))

@login_required()
def delete_law(request, pk):
    tmp = get_name()
    button = get_button()
    template = loader.get_template('laws/delete.html')
    object_list = get_object_or_404(Law, pk=pk)
    if request.method == 'POST':
        object_list.delete()
        return HttpResponseRedirect(reverse('laws:show'))
    else:
        context = {
            'title': get_body(tmp[3], tmp[0]),
            'object_list': object_list,
            'uri': get_url('laws'),
            'button': button[3],
        }
    return HttpResponse(template.render(context, request))