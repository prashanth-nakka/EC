from django.shortcuts import render


# Create your views here.
def home(requst):
    return render(requst, 'store/index.html')