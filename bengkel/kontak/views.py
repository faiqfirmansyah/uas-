from django.shortcuts import render
from .forms import formkon

def kont(request):
    form = formkon()

    context = {
        'form': form,
    }
    return render(request,'kontak.html',context)