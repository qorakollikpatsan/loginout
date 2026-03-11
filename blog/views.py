from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


@login_required
def home(request):
    return render(request, 'home.html')


@login_required
def about(request):
    return render(request, 'about.html')


def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/login')

    context = {'form': form}
    return render(request, 'register.html', context)


@login_required
def profile(request):
    user = request.user
    context = {'user': user}
    return render(request, 'profile.html', context)



