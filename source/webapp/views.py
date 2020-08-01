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


def guest_book_update_view(request, pk):
    guest_book = get_object_or_404(GuestBook, pk=pk)
    if request.method == "GET":
        form = GuestBookForm(initial={
            'author': guest_book.author,
            'email': guest_book.email,
            'text': guest_book.text
        })
        return render(request, 'guest_book_create.html', context={
            'form': form,
            'guest_book': guest_book
        })
    elif request.method == 'POST':
        form = GuestBookForm(data=request.POST)
        if form.is_valid():
            guest_book.author = form.cleaned_data['author']
            guest_book.email = form.cleaned_data['email']
            guest_book.text = form.cleaned_data['text']
            guest_book.save()
            return redirect('index')
        else:
            return render(request, 'guest_book_create.html', context={
                'guest_book': guest_book,
                'form': form
            })
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])


def guest_book_delete_view(request, pk):
    guest_book = get_object_or_404(GuestBook, pk=pk)
    if request.method == 'GET':
        return render(request, 'guest_book_delete.html', context={'guest_book': guest_book})
    elif request.method == 'POST':
        guest_book.delete()
        return redirect('index')
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])