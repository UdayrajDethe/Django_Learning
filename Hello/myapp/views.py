from django.shortcuts import render, HttpResponse
from django.http import JsonResponse

# Create your views here.
def home(request):
    # return HttpResponse('This is Home Pages')
    context={
        "name" : "uday",
        "lastname" : "dethe"
    }

    # return JsonResponse(context, safe=False)
    return render(request, 'index.html', context.name)

def about(request):
    # return HttpResponse('This is about Pages')

    return render(request, 'about.html')

def service(request):
    # return HttpResponse('This is service Pages')
    return render(request, 'service.html')

def contact(request):
    return HttpResponse('This is Contact Pages')
