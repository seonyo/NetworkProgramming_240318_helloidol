from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def say_hello(request):
    return HttpResponse("Hello World")

def say_hello_html(request):
    return render(request, "playground/hello.html", {'name': '지우야', 'greeting': '안녀엉~'})

def say_bye_html(request):
    context = {
        'singer' : 'Toil',
        'title' : '네 옆에 그 사람은 내가 아닌 다른 사람'
    }
    return render(request, "playground/bye.html", context=context)