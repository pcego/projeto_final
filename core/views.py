from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'core/index.html')


@login_required()
def board(request):
    data = []
    return render(request, 'core/board.html', data)
