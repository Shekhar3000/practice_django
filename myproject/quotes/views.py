from django.shortcuts import render
from django.shortcuts import redirect

from .models import Quote

def quote_list(request):
    quotes = Quote.objects.all()
    return render(request, 'quotes/list.html', {'quotes': quotes})


def add_quote(request):
    if request.method == "POST":
        author = request.POST.get('author')
        text = request.POST.get('text')
        Quote.objects.create(author=author, text=text)
        return redirect('/quotes/')
    return render(request, 'quotes/add.html')