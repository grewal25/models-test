from django.shortcuts import render, get_object_or_404

from . models import Choice, Question

def index(request):
    total_question=Question.objects.order_by('-pub_date')
    return render(request, 'polls/index.html', {'total_question':total_question})

def detail(request, question_ids):
    questions=get_object_or_404(Question, pk=question_ids)
    return render(request, 'polls/detail.html', {'questions':questions})
