from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'market3d/home.html')