from django.shortcuts import render
from .models import Post
from django.views.generic import TemplateView

def home(request):
    return render(request, 'home.html', {})

class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class MypagePageView(TemplateView):
    template_name = 'mypage.html'
