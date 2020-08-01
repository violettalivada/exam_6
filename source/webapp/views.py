from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotAllowed
from webapp.models import GuestBook


def index_view(request):
    is_admin = request.GET.get('is_admin', None)
    if is_admin:
        data = GuestBook.objects.all()
    else:
        data = GuestBook.objects.filter(status='active')
    return render(request, 'index.html', context={
        'guestbook': data
    })
