from django.shortcuts import render
from .models import servis

def ser(request):
    model = servis.objects.all()

    context = {
        'model': model,
    }
    return render(request,'servis.html',context)

