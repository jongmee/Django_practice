from django.shortcuts import get_object_or_404, render, redirect
from .models import reservationModel, Menu, MenuReservation, Review
from django.utils import timezone
from .forms import menuReservationForm, ReviewForm

from django.contrib import auth
from django.contrib.auth import get_user_model

User = get_user_model()  # 이거 꼭 기억하기


# redirect는 url name으로, render는 request와 함께 .html로

def mainPage(request):
    return render(request, 'index.html')


def booking(request):
    if (request.method == 'POST'):
        new = reservationModel()
        new.name = request.POST['name']
        new.email = request.POST['email']
        new.phone = request.POST['phone']
        new.people = request.POST['people']
        new.dateCurrent = timezone.now()
        new.date = request.POST['date']
        new.time = request.POST['time']
        new.message = request.POST['message']
        new.save()
        return redirect('bookFinish')
    return render(request, 'reservation.html')


def bookingFinish(request):
    return render(request, 'reservation_finish.html')


def Chef(request):
    return render(request, 'chef.html')


def menu(request):
    menus_starter = Menu.objects.filter(
        menu_type='starters').order_by('menu_name')
    menus_breakfast = Menu.objects.filter(
        menu_type='breakfast').order_by('menu_name')
    menus_lunch = Menu.objects.filter(menu_type='lunch').order_by('menu_name')
    menus_dinner = Menu.objects.filter(
        menu_type='dinner').order_by('menu_name')
    return render(request, 'menu.html', {"menus_starter": menus_starter, "menus_breakfast": menus_breakfast, "menus_lunch": menus_lunch, "menus_dinner": menus_dinner})

# model form 으로 예약 받고 각 메뉴에 따라(pk 이용) 예약 내역 저장하기


def menu_reservation(request, menu_id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = menuReservationForm(request.POST)
            if form.is_valid():
                reser = MenuReservation()
                reser.date = form.cleaned_data['date']
                reser.time = form.cleaned_data['time']
                reser.menu_info = get_object_or_404(Menu, pk=menu_id)
                reser.client_info = request.user
                reser.save()
                return redirect('bookFinish')
        else:
            form = menuReservationForm()
            form_review = ReviewForm()
            menu = get_object_or_404(Menu, pk=menu_id)
            reviews = Review.objects.filter(review_menu = menu)
        return render(request, 'menu_reservation.html', {'menu': menu, 'form': form ,'form_review': form_review, 'reviews': reviews})
    return redirect('home')

def menu_review(request, menu_id):
    filled_form = ReviewForm(request.POST)
    if filled_form.is_valid():
        finished_form=filled_form.save(commit=False)
        finished_form.review_menu = get_object_or_404(Menu, pk=menu_id)
        finished_form.save()
    return redirect('menu_reservation', menu_id)
