# coding=utf-8
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from . import models


def paginate(objects_list, per_page, request):
    paginator = Paginator(objects_list, per_page)
    page = request.GET.get('page')
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        # В случае, GET параметр не число
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)
    return questions, paginator


# questions

def questions_list(request):
    qu_list = list(models.Question.objects.get_last())
    paginator = paginate(qu_list, 10, request)  # per page fixme

    return render(request, 'index.html', {'index_name': 'Last questions',
                                          'questions': paginator[0],
                                          'paginator': paginator[1]})


def hot_list(request):
    qu_hot_list = list(models.Question.objects.get_hot())
    paginator = paginate(qu_hot_list, 10, request)

    return render(request, 'index.html', {'index_name': 'Popular questions',
                                          'questions': paginator[0],
                                          'paginator': paginator[1]})


def question(request, id):
    try:
        # id = request.GET.get('id')
        qu = models.Question.objects.get(pk=id)
    except models.Question.DoesNotExist:
        return HttpResponseNotFound()
    # todo paginate
    answers = list(models.Answer.objects.get_answers(id))
    return render(request, 'question.html', {'qu': qu, 'answers': answers})


@login_required(login_url=reverse_lazy('user_login'))
def ask_question(request):
    return render(request, 'ask.html', {'tag_name': 'ha'})


def tag_list(request, tag_name):
    qu_tag_list = list(models.Question.objects.get_by_tag(tag_name))
    paginator = paginate(qu_tag_list, 10, request)

    return render(request, 'index.html', {'questions': paginator[0],
                                          'paginator': paginator[1],
                                          'index_name': '#' + tag_name})


# user

def user_login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('questions_list'))
    user = authenticate(request)
    if user is None:  # failure
        return HttpResponseRedirect(reverse('user_login'))
    else:
        return HttpResponseRedirect(reverse('questions_list'))


def user_logout(request):
    pass


@login_required(login_url=reverse_lazy('user_login'))
def user_settings(request):
    return render(request, 'settings.html', {'tag_name': 'zs'})


def user_signup(request):
    if request.user.is_authenticated:
        return questions_list(request)
    return render(request, 'signup.html', {'tag_name': 'za'})
