from django.shortcuts import render
from .forms import UserForm
import random


def index(request):
    submitbutton = request.POST.get("submit")
    rand =random.randrange(1,100,1)

    number = 0
    diff=0


    form = UserForm(request.POST or None)
    if form.is_valid():
        number = form.cleaned_data.get("number")

    if number > rand:
        data = 'greter'
        diff = number - rand
    elif number <rand:
        data ='lesthan'
        diff = rand -number
    else:
        data = 'equal'




    context = {'form': form, 'number': number,
               'submitbutton': submitbutton,'rand':rand,'data':data,'diff':diff}


    return render(request, 'guess/home.html', context)

