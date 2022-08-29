from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from django.urls import reverse


def main(request: HttpRequest) -> JsonResponse:
    print(reverse('main-url'))
    return JsonResponse(data={
        "error": False,
        "status": "Hello from Django",
        "detailt": None
    }, status=200)


def index(request: HttpRequest):
    return render(request, 'index.html')



def login(request: HttpRequest):
    return render(request, 'sign-in.html')


def signup(request: HttpRequest):
    return render(request, 'sign-up.html')




