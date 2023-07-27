from django.shortcuts import redirect
from django.views.generic import ListView

from project.library.models import Book


def RedirectHomeView(request):
    '''
    Redirect url from '/' to '/home/'
    '''
    return redirect('home')


class HomeView(ListView):
    '''
    Renders home page with all the products
    '''
    template_name = 'project/home.html'
    model = Book

    def get(self, request):
        return super().get(request)
