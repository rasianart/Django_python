from django.shortcuts import render

from django.http import HttpResponse

from django.http import HttpResponseRedirect
# from django.http import Redirect

from .models import User

from .forms import PostForm

def index(request):

    context = { 'name' : 'Adonis', 'users' : User.objects.all() }

    return render(request, 'users/index.html', context)

def detail(request):

    context =  { 'user' : User.objects.get(first_name='Jane') }

    return render(request, 'users/detail.html', context)

def add(request):


    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PostForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            # return HttpResponseRedirect('/submitted/')
            return HttpResponseRedirect('/submitted/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PostForm()

    context = { 'form': form, 'header' : 'This is the add view!', 'route': '/index'}

    return render(request, 'users/add.html', context)

def submitted(request):

    context = { 'submitted' : 'Successfully Submited!' }

    return render(request, 'users/submitted.html', context)
