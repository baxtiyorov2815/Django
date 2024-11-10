from django.shortcuts import render, HttpResponse


def home(request):
    text = "<h2>Home Page</h2>"
    return HttpResponse(text)


def about(request):
    text = "<h2>About Us</h2>"
    return HttpResponse(text)


def contact(request):
    text = "<h2>Contact: +998936902815</h2>"
    return HttpResponse(text)
