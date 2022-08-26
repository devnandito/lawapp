# coding=utf-8

# Django
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.views.generic import ListView

# Models
from lawapp.articles.models import Article

# Forms
from lawapp.articles.forms import ArticleForm

# Utilities
from lawapp.utils.functions import get_url, get_body, get_button
import json

def get_name():
    name = ['Articulos', 'articulos', 'Articulo', 'articulo']
    return name

@login_required()
def show_article(request):
    tmp = get_name()
    list_title = ['Ley', 'Capitulo', 'Articulo', 'Descripcion', 'Acciones']
    template = loader.get_template('articles/show.html')
    list_paginator = Article.objects.order_by('fklaw', 'num')
    paginator = Paginator(list_paginator, 6)
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
        'uri': get_url('articles'),
        'list_title': list_title,
    }
    return HttpResponse(template.render(context, request))

@login_required()
def create_article(request):
    tmp = get_name()
    button = get_button()
    template = loader.get_template('articles/add.html')
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            message = 'Los datos se guardaron correctamente!'
            tpl = loader.get_template('messages/message.html')
            contextSuccess = {
                'title': get_body(tmp[3], tmp[0]),
                'uri': get_url('articles'),
                'message': message,
            }
            return HttpResponse(tpl.render(contextSuccess, request))
    else:
        form = ArticleForm()
    context = {
        'title': get_body(tmp[3], tmp[0]),
        'form': form,
        'uri': get_url('articles'),
        'button': button[1],
    }
    return HttpResponse(template.render(context, request))

@login_required()
def edit_article(request, pk):
    tmp = get_name()
    button = get_button()
    template = loader.get_template('articles/edit.html')
    ins = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=ins)
        if form.is_valid():
            form.save()
            message = 'Los datos se guardaron correctamente!'
            tpl = loader.get_template('messages/message.html')
            contextSuccess = {
                'title': get_body(tmp[3], tmp[0]),
                'uri': get_url('articles'),
                'message': message,
            }
            return HttpResponse(tpl.render(contextSuccess, request))
    else:
        form = ArticleForm(instance=ins)
    context = {
        'title': get_body(tmp[3], tmp[0]),
        'form': form,
        'uri': get_url('articles'),
        'button': button[1],
    }
    return HttpResponse(template.render(context, request))

@login_required()
def delete_article(request, pk):
    tmp = get_name()
    button = get_button()
    template = loader.get_template('articles/delete.html')
    object_list = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        object_list.delete()
        return HttpResponseRedirect(reverse('articles:show'))
    else:
        context = {
            'title': get_body(tmp[3], tmp[0]),
            'object_list': object_list,
            'uri': get_url('articles'),
            'button': button[3],
        }
    return HttpResponse(template.render(context, request))

def print_format(value):
    value = str('{}'.format(value))
    return value

def print_uri_edit(value, path):
    value = str('../edit/{}/{}'.format(value, path))
    return value

def print_uri_delete(value, path):
    value = str('../delete/{}/{}'.format(value, path))
    return value

@login_required()
def show_article_json(request):
    object_list = Article.objects.all()
    path = 'article'
    data = [{
        '#': item.id,
        'chapter': print_format(item.fkchapter),
        'num': print_format(item.num),
        'des': print_format(item.description),
        'action': '<div class="btn-group"><a href="'+print_uri_edit(item.id, path)+
            '" class="btn btn-warning"><i class="fa fa-pencil"></i></a><a href="'
            +print_uri_delete(item.id,path)+'" class="btn btn-danger"><i class="fa fa-times"></i></a></div>',
        } for item in object_list]
    json_data = json.dumps(data)
    return HttpResponse(json_data, content_type="application/json")

@login_required()
def show_article_json1(request):
    json_data = json.dumps(list(Article.objects.values('fklaw__title', 'fkchapter', 'num', 'description')))
    return HttpResponse(json_data, content_type="application/json")

class ArticleListView(ListView):
    model = Article
    template_name = 'articles/article_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['qs_json'] = json.dumps(list(Article.objects.values('fklaw__title', 'fkchapter', 'num', 'description')))
        return context

@login_required()
def show_article_json2(request):
    tmp = get_name()
    list_title = ['Ley', 'Capitulo', 'Articulo', 'Descripcion', 'Acciones']
    template = loader.get_template('articles/list.html')
    list_paginator = Article.objects.order_by('fklaw', 'num')
    qs_json = json.dumps(list(Article.objects.values('fklaw__title', 'fkchapter__description', 'num', 'description')))
    paginator = Paginator(list_paginator, 6)
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
        'uri': get_url('articles'),
        'list_title': list_title,
        'qs_json': qs_json,
    }
    return HttpResponse(template.render(context, request))