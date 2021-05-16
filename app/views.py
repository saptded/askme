from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import *

context = {
    'best_users': Profile.objects.all(),
    'hot_tags': Tag.objects.all(),
}


def paginate(objects_list, request, per_page=5):
    cl = list(objects_list)
    paginator = Paginator(cl, per_page)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.get_page(1)
    except EmptyPage:
        page_obj = paginator.get_page(paginator.num_pages)
    print("hello drujok-pirojok")
    return page_obj


def new_questions(request):
    tag_list = Tag.objects.all()[:10]
    latest_question_list = Question.objects.get_new()
    page_obj = paginate(latest_question_list, request)
    return render(request, 'new_questions.html', {'questions': page_obj, 'tags': tag_list})


def hot_questions(request):
    tag_list = Tag.objects.all()[:10]
    hot_question_list = Question.objects.hot()
    page_obj = paginate(hot_question_list, request)
    return render(request, 'hot_questions.html', {'questions': page_obj, 'tags': tag_list})


def ask(request):
    tag_list = Tag.objects.all()[:10]

    return render(request, 'ask.html', {'tags': tag_list})


def login(request):
    tag_list = Tag.objects.all()[:10]

    return render(request, 'login.html', {'tags': tag_list})


def open_question(request, qid):
    tag_list_all = Tag.objects.all()[:10]
    question = Question.objects.get(pk=qid)
    comments_list = list(question.comment_set.all())
    page_obj = paginate(comments_list, request, 5)
    tag_list = question.tags.all()[:5]

    return render(request, 'open_question.html',
                  {'question': question, 'comments': page_obj, 'tags': tag_list_all, 'question_tags': tag_list})


def settings(request):
    tag_list = Tag.objects.all()[:10]

    return render(request, 'settings.html', {'tags': tag_list})


def signup(request):
    tag_list = Tag.objects.all()[:10]

    return render(request, 'signup.html', {'tags': tag_list})


def tag_page(request, tid):
    tag_list = Tag.objects.all()[:10]
    tag = Tag.objects.get(tag_title=tid)
    latest_question_list = tag.question_set.all()
    page_obj = paginate(latest_question_list, request)
    return render(request, 'tag.html', {'tag': tid, 'questions': page_obj, 'tags': tag_list})
