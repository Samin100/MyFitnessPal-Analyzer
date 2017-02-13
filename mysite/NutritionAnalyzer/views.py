from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, 'NutritionAnalyzer/home.html', {'content': ['If you would like to contact me please email me', 'samin100@gmail.com']})


def analysis(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        date = request.POST['date']
        print(username)
        print(password)
        print(date)
