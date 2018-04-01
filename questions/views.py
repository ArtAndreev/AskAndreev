# coding=utf-8
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render

QUESTIONS = {
    '1': {'id': 1, 'title': 'I`m your dream', 'text': 'I`m your dream, make you real'},
    '2': {'id': 2, 'title': 'I`m your eyes', 'text': 'I`m your eyes when you must steal'},
    '3': {'id': 3, 'title': 'I`m your pain', 'text': 'I`m your pain when you can`t feel'},
}


def paginate(objects_list, request):
    paginator = Paginator(objects_list, 30)
    page = request.GET.get('page')
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        # В случае, GET параметр не число
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)
    return objects_page, paginator


def questions_list(request):
    # if (hot)
    contact_list = list(QUESTIONS.values())
    paginator = Paginator(contact_list, 20)

    page = request.GET.get('page')
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        # В случае, GET параметр не число
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)

    return render(request, 'index.html', {'user_is_signed_in': True, 'questions': questions, 'user_name': 'Vasya Pupok'})


def hot_list(request):
    contact_list = list(QUESTIONS.values())
    paginator = Paginator(contact_list, 20)

    page = request.GET.get('page')
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        # В случае, GET параметр не число
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)

    return render(request, 'index.html', {'questions': questions})


def question(request, question_id):
    return render(request, 'question.html', {'question': QUESTIONS.get(question_id, {})})


def ask_question(request):
    return render(request, 'ask.html', {'tag_name': 'ha'})


def tag_list(request, tag_name):
    return render(request, 'tag.html', {'tag_name': tag_name})


def user_login(request):
    return render(request, 'login.html', {'tag_name': 'zs'})


def user_settings(request):
    return render(request, 'settings.html', {'tag_name': 'zs'})


def user_signup(request):
    return render(request, 'signup.html', {'tag_name': 'za'})
