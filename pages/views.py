from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def Home_view(request, *args, **kwargs):
    # return HttpResponse('<h1>Hello World...</h>')
    return render(request, 'Home.html', {})


def Contact_view(request, *args, **kwargs):
    # return HttpResponse('<h1>Contact page</h>')
    return render(request, 'Contact.html', {})


def About_view(request, *args, **kwargs):
    my_context = {
        "my_text": "This is about us",
        "my_number": 123456,
        "my_list": [123, 312, 345, "Abc"]
    }
    return render(request, 'About.html', my_context)
