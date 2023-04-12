from django.shortcuts import render

# Create your views here.
def mdb4parent(request):
    return render(request,'mdb4parent.html')


def mdb4child(request):
    return render(request,'mdb4child.html')    