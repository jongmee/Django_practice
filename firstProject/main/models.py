from http import client
from tkinter import CASCADE
from django.db import models
from accounts import views
from accounts.models import User
from django.utils import timezone


class reservationModel(models.Model):  # 예약 정보
    name = models.CharField(max_length=20)  # 예약자 이름
    email = models.EmailField(max_length=50)  # 예약자 이메일
    phone = models.CharField(max_length=12)  # 예약자 전화번호
    dateCurrent = models.DateTimeField(auto_now_add=True)  # 예약을 실행한 시각
    date = models.IntegerField()  # 예약 날짜
    time = models.IntegerField()  # 예약 시간
    people = models.IntegerField(default=0)  # 사람 수
    message = models.CharField(max_length=200)  # 예약 시 메모

    def __str__(self):
        return self.name


class Menu(models.Model):
    TYPE_CHOICES = {
        ('starters', 'Starters'),
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner')
    }
    menu_image = models.ImageField(blank=True, null=True, upload_to='images/')
    menu_name = models.CharField(max_length=20)
    menu_cost = models.FloatField()
    menu_type = models.CharField(
        choices=TYPE_CHOICES, max_length=20, null=True)
    # menu_ingredient= (이거 리스트로 어떻게 구현하지?)

    def __str__(self):
        return self.menu_name


class Review(models.Model):
    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    body = models.TextField(max_length=5000, null=True)
    date = timezone.now()
    review_menu = models.ForeignKey(Menu, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.body


class MenuReservation(models.Model):
    menu_info = models.ForeignKey(Menu, on_delete=models.CASCADE)
    client_info = models.ForeignKey(User, on_delete=models.CASCADE)
    dateCurrent = models.DateTimeField(auto_now_add=True)  # 예약을 실행한 시각
    date = models.IntegerField()  # 예약 날짜
    time = models.IntegerField()  # 예약 시간

    def __str__(self):
        return self.menu_info.menu_name
