from django.http import HttpResponse
from django.shortcuts import render
# from . import test5
from .test5 import select_book_by_name

# Create your views here.

def index(request):
    if request.POST:
        args = {}
        if 'b1' in request.POST:
            s = request.POST.get('t1')
            response = select_book_by_name(s)
            args['response'] = response


    return render(request, 'app/index.html', args)