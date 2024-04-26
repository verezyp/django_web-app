from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import requires_csrf_token
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


def pilot(request):
    return render(request, 'test2.html', {})


@login_required
def main(request):
    return render(request, 'main.html', {})