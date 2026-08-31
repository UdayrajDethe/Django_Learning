from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    #//return {"message" : "Welcome to our website"}
    #? Django communicate with browser using HTTP responses not a raw python string or dictionary
    # return HttpResponse("Welcome to our website")
    #//return HttpResponse('<h1>Welcome to our website</h1>')

    return render(request, "home.html")
    """
    return HttpResponse('''
    <html>
        <body>
            <h1> Home <h1>
            <a href='home/' > Home</a>
            <a href='about/' > About</a>
            <a href='contant/' > Contant</a>
        <body>
    </html>
    ''')
    """

#! This is just a one simple page it not a page only. What if we need to display a real page in that way this not a way to write a html code in python function that why we Go For Templates

def contactus(request):
    return render(request, "contact.html")

def about(request):
    return render(request, "about.html")
