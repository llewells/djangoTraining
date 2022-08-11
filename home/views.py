from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


## Function BAsed views
# def home(request):
#     return render(request, 'home/welcome.html', {'today':datetime.today()})

# @login_required(login_url='/admin')
# def authorized(request):
#     return render(request, 'home/authorized.html', {})

## Class Based Views
class HomeView(TemplateView):
    '''class based view'''
    template_name = 'home/welcome.html'
    extra_context = {'today': datetime.today()}

class AuthView(LoginRequiredMixin, TemplateView):
    template_name = 'home/authorized.html'
    login_url = '/admin'
