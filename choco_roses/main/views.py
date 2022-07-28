from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from django.urls import reverse
from .models import RoseColor


def main(request: HttpRequest) -> JsonResponse:
    print(reverse('main-url'))
    return JsonResponse(data={
        "error": False,
        "status": "Hello from Django",
        "detailt": None
    }, status=200)



def foo(x):
    return x+1