from django.http import HttpResponse
from django.shortcuts import render
from app.Select_book import select_book
from app.Order import open_order
import string

# from . import test5

# Create your views here.


def index(request):
    args = {}
    if request.POST:
        if 'b1' in request.POST:
            name = request.POST.get('t1')
            autor = request.POST.get('t2')
            genre = request.POST.get('t3')
            response = select_book([name, autor, genre])
            args['response'] = response


    return render(request, 'app/index.html', args)

def lol(request):
    args = {}
    if request.POST:
        if 'b3' in request.POST:
            book_id = request.POST.get('t10')
            first_name = request.POST.get('t5')
            second_name = request.POST.get('t6')
            email = request.POST.get('t7')
            phone_number = request.POST.get('t8')
            delivery_address = request.POST.get('t9')
            print(book_id)
            response = open_order(book_id,first_name, second_name, email, phone_number, delivery_address)
            args['response'] = response

    return render(request, 'app/lol.html', args)




"""
def index(request):
    args = {}
    if request.POST:
        if 'b1' in request.POST:
            name = request.POST.get('t1')
            name1 = request.POST.get('t2')
            name2 = request.POST.get('t3')
            response = name + name1 + name2
            name = request.POST.get('t1')
            autor = request.POST.get('t2')
            genre = request.POST.get('t3')
            response = select_book([name, autor, genre])
            print(response)
            args['response'] = response


    return render(request, 'app/index.html', args)

def lol(request):
    return render(request, 'app/lol.html')
"""
'''
def index(request):
    args = {}
    if request.POST:
        if 'b1' in request.POST:
            name = request.POST.get('t1')
            autor = request.POST.get('t2')
            genre = request.POST.get('t3')
            response = select_book([name, autor, genre])
            args['response'] = response


    return render(request, 'app/index.html', args)'''
