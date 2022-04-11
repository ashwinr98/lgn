from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

from django.db import models
from django import forms
import requests


# Create your views here.
class tckrsymbol(models.Model):
    ticker = models.CharField(max_length=5)

    def get_absolute_url(self):
        return "results/"
class searchform(forms.ModelForm):
    class Meta:
        model = tckrsymbol
        fields = ('ticker',)
def home(request):
    return render(request,"users/home.html")



class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "users/signup.html"

class TickerSearch(CreateView):
    model = tckrsymbol
    template_name = 'stock/search.html'
    form_class = searchform

def Analysis(request):
    stock = str(tckrsymbol.objects.last().ticker)
    
    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol='+ stock + '&interval=5min&apikey=3VLLLPTTVJO8QNDK'
    print(url)
    r = requests.get(url)
    
    data = r.json()
    
    last_time = data['Meta Data']['3. Last Refreshed']
    stock_val = {'val':data['Time Series (5min)'][last_time]['2. high']}
    print(stock_val)
    return render(request, 'stock/stk_results.html', stock_val)