from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import eventlist
from .forms import EventForm

# Create your views here.
def index(request):
    event = eventlist.objects.all()
    likedEvent = eventlist.objects.filter(is_liked=request.user.id)
    return render(request, 'event/index.html', {'events':event, 'likedEvent':likedEvent})

def signin(request):
    if request.method=="POST":
        email = request.POST['email']
        frstname = request.POST['frstname']
        lastname = request.POST['lastname']
        password = request.POST['password']
        newUser = User.objects.create_user(email, email, password)
        newUser.first_name = frstname
        newUser.last_name = lastname
        newUser.save()
        messages.success(request, "Your account has been successully created")
    return render(request, 'event/signin.html')

def logIn(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('/event')
        else:
            messages.error(request, "Invalid credentials!")
    return render(request, 'event/login.html')

def logOut(request):
    logout(request)
    event = eventlist.objects.all()
    return render(request, 'event/index.html', {'events':event})

@login_required(login_url='/event/login')
def createEvent(request):
    if request.method=="POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Event Successfully Created")
    else:
        form = EventForm()
    return render(request, 'event/create.html', {'form':form})

@login_required(login_url='/event/login')
def likedEvents(request):
    event = eventlist.objects.filter(is_liked=request.user.id)
    return render(request, 'event/liked.html', {'events':event})

@login_required(login_url='/event/login')
def like(request):
    if request.POST.get('action') == 'post':
        result = ''
        id = int(request.POST.get('id'))
        event = get_object_or_404(eventlist, id=id)
        print(event)
        if event.is_liked.filter(id=request.user.id).exists():
            event.is_liked.remove(request.user)
            event.save()
            result = 'unlike'
        else:
            event.is_liked.add(request.user)
            event.save()
            result = 'like'
        return JsonResponse({'result':result})
