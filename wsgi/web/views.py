from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.contrib import auth
# Create your views here.
def index(request):
    return render(request, 'index.html')



def gift(request):
    return render(request, 'gift.html')

def test(request):
    return render(request, 'test.html')