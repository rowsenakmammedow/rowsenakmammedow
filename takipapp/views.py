from django.shortcuts import render
 
def index(request):
    return render(request, 'index.html')


def track(request):
    return render(request, 'track.html')
