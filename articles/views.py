from django.shortcuts import render
from .models import Articles
from django.views.generic import ListView, DetailView
from .forms import UserForm

# Create your views here.

class ArticleListView(ListView):
    model = Articles
    template_name = 'home.html'


class ArticleDetailView(DetailView):
    model = Articles
    template_name = 'detail.html'
    context_object_name = 'details'


def form_page(request):
    form = UserForm()
    dict_obj = { 'form' : form}
    return render(request, './form_page.html', dict_obj)

def thanks_page(request):
    if request.POST:
        title = request.POST['title']
        body = request.POST['body']
        image = request.POST['image']
        element = Articles(title = title, body = body, image = image)
        element.save()
        return render(request, './thanks.html')
    else:
        return render(request, './thanks.html')