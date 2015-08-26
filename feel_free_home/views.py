from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def thankyou(request):
    return render(request, 'thankyou.html')

def signUpTest(request):
    print "yes"
    return render(request, 'index.html')
