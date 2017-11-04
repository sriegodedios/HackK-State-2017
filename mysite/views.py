from django.http import HttpResponse


def index(request):
    return HttpResponse('<p>Hello, world. You\'re at the true index.</p><a href="/history/">history</a>')