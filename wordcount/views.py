from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    context = {
        'datatext' : 'Welcome To My Page'
    }
    return render(request, 'home.html', context)

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    context = {
        'datatext' : 'Counting Page',
        'fulltext' : fulltext,
        'count' : len(wordlist),
    }

    return render(request, 'count.html', context)

def about(request):
    context = {
        'company' : 'LEXLINK Information Technology Services'
    }
    return render(request, 'about.html', context)