from .forms import TripForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Trip
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


@login_required
def create_trip(request):
    if request.method == 'POST':
        form = TripForm(request.POST, request.FILES)
        if form.is_valid():
            trip = form.save(commit=False)
            trip.user = request.user
            trip.latitude = request.POST.get('latitude')
            trip.longitude = request.POST.get('longitude')
            trip.save()
            return redirect('trip_detail', trip_id=trip.id)
    else:
        form = TripForm()
    return render(request, 'trips/create_trip.html', {'form': form})


def trip_detail(request, trip_id):
    trip = get_object_or_404(Trip, id=trip_id)
    return render(request, 'trips/trip_detail.html', {'trip': trip})

def trip_list(request):
    if request.user.is_authenticated:
        trips = Trip.objects.filter(user=request.user)
    else:
        trips = []
    return render(request, 'trips/trip_list.html', {'trips': trips})

def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('trip_list')
    else:
        form = UserCreationForm()
    return render(request, 'trips/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('trip_list')
            else:
                form.add_error(None, 'Неверное имя пользователя или пароль.')
    else:
        form = AuthenticationForm()
    return render(request, 'trips/login.html', {'form': form})


def ustr_logout(request):
    logout(request)
    return redirect('trip_list')

def is_admin(user):
    return user.is_staff