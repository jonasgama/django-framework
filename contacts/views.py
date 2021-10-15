from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def ok(request):
    return JsonResponse("OK", safe=False)
