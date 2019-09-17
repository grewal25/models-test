from django.shortcuts import render
from . models import Group, Person


def home(request):
    all_names=Person.objects.order_by('-name')[:5]
    return render(request, 'likes/home.html',{'all_names':all_names})

def detail(request, person_id):
    group_likes=Person.objects.get(pk=person_id)
    return render(request, 'likes/detail.html', {'group_likes':group_likes})
