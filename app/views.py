from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .models import *

questions = [
    {
        'id': idx,
        'title': f'Title number {idx}',
        'text': f'Text for question {idx}',
        'answers': idx,
        'tag': f'tag {idx}',
        'tag1': f'tag {idx + 1}',
        'tag2': f'tag {idx + 2}',
    } for idx in range(15)
]

n_questions = [
    {
        'id': idx,
        'title': f'NEW Title number {idx}',
        'text': f'NEW Text for question {idx}',
        'answers': idx,
        'tag': f'tag {idx}',
        'tag1': f'tag {idx + 1}',
        'tag2': f'tag {idx + 2}',
    } for idx in range(25)
]

tag_questions = [
    {
        'id': idx,
        'title': f'NEW Title number {idx}',
        'text': f'NEW Text for question {idx}',
        'answers': idx,
        'tag': f'tag {0}',
        'tag1': f'tag {idx + 1}',
        'tag2': f'tag {idx + 2}',
    } for idx in range(10)
]

pop_tags = [
    {
        'tag1': f'tag',
        'tag2': f'tag2',
        'tag3': f'tag3',
        'tag4': f'tag4',
        'tag5': f'tag5',
        'tag6': f'tag6',
        'tag7': f'tag7',
        'tag8': f'tag8',
        'tag9': f'tag9',
    } for idx in range(1)
]


def paginate(objects_list, request, per_page=5):
    cl = list(objects_list)
    paginator = Paginator(cl, per_page)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        # В случае, GET параметр не число
        page_obj = paginator.get_page(1)
    except EmptyPage:
        page_obj = paginator.get_page(paginator.num_pages)
    print("hello drujok-pirojok")
    return page_obj


def new_questions(request):
    tag_list = Tag.objects.all()[:10]
    latest_question_list = Question.objects.all()
    page_obj = paginate(latest_question_list, request)
    return render(request, 'new_questions.html', {'questions': page_obj, 'tags': tag_list})


def hot_questions(request):
    page_obj = paginate(questions, request)
    return render(request, 'hot_questions.html', {'questions': page_obj, 'pop_tags': pop_tags})


def ask(request):
    return render(request, 'ask.html', {'pop_tags': pop_tags})


def login(request):
    return render(request, 'login.html', {'pop_tags': pop_tags})


def open_question(request, pk):
    question = questions[pk]
    page_obj = paginate(questions, request)
    return render(request, 'open_question.html', {'question': question, 'questions': page_obj, 'pop_tags': pop_tags})


def settings(request):
    return render(request, 'settings.html', {'pop_tags': pop_tags})


def signup(request):
    return render(request, 'signup.html', {'pop_tags': pop_tags})


def tag_page(request, tid):
    tag_list = Tag.objects.all()[:10]
    tag = Tag.objects.get(tag_title=tid)
    latest_question_list = tag.question_set.all()
    page_obj = paginate(latest_question_list, request)
    return render(request, 'tag.html', {'tag': tid, 'questions': page_obj, 'pop_tags': tag_list})
