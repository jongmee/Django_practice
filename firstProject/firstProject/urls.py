from django.contrib import admin
from django.urls import path
from accounts import views as accountViews
from main import views as mainViews

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainViews.mainPage, name='home'),
    path('booking/', mainViews.booking, name='book'),
    path('booking/finish', mainViews.bookingFinish, name='bookFinish'),
    path('chef/', mainViews.Chef, name='Chef'),
    path('menu/', mainViews.menu, name='menu'),
    path('menu-reservation/<int:menu_id>', mainViews.menu_reservation, name='menu_reservation'),
    path('menu-reservation/review/<int:menu_id>', mainViews.menu_review, name='menu_review'),


    path('login/', accountViews.login, name='loginPage'),
    path('logout/', accountViews.logout, name='logoutPage'),
    path('sign-up/', accountViews.signUp, name='sign-up'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
