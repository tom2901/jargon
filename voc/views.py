from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    return render(request, 'voc/index.html')

def login(request):
    context = {}
    return render(request, 'voc/login.html')

def register(request):
    context = {}
    return render(request, 'voc/register.html')

def main(request):
    context = {}
    return render(request, 'voc/main.html')

def train(request):
    context = {}
    return render(request, 'voc/train.html')
