import random

from django.shortcuts import render, redirect

from taskify.inspiration import INSPIRATIONAL_QUOTES


def index(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    random_quote = random.choice(INSPIRATIONAL_QUOTES)
    context = {
        'random_quote': random_quote
    }
    return render(request, 'common/index.html', context)


def about(request):
    return render(request, 'common/about.html')