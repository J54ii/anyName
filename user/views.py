from django.shortcuts import render
from .forms import UserCreationForm
# Create your views here.


def regs(request):
    form = UserCreationForm()
    return render(request, 'user/register.html' , {
        'title' : 'التسجيل',
        'from' : form,
    })