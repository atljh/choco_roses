from django.contrib.auth.models import User
from django.http import JsonResponse


def validate_number(request):
    number = request.GET.get('number')

    result = number > 0 and len(number) > 100
    print(result)

    data = {
       'result': result
    }
    return JsonResponse(data)

