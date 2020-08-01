from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotAllowed
from webapp.models import GuestBook
from webapp.forms import GuestBookForm


def index_view(request):
    is_admin = request.GET.get('is_admin', None)
    if is_admin:
        data = GuestBook.objects.all()
    else:
        data = GuestBook.objects.filter(status='active')
    return render(request, 'index.html', context={
        'guest_books': data
    })


def guest_book_create_view(request):
    if request.method == "GET":
        form = GuestBookForm()
        return render(request, 'guest_book_create.html', context={
            'form': form
        })
    elif request.method == 'POST':
        form = GuestBookForm(data=request.POST)
        if form.is_valid():
            GuestBook.objects.create(
                author=form.cleaned_data['author'],
                email=form.cleaned_data['email'],
                text=form.cleaned_data['text']
            )
            return redirect('index')
        else:
            return render(request, 'guest_book_create.html', context={
                'form': form
            })
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])