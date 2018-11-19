from django.urls import path
from . import views
from .views import AboutPageView, HomePageView, MypagePageView

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('home/', HomePageView.as_view(), name='home'),
    path('mypage/', MypagePageView.as_view(), name='mypage'),
]
