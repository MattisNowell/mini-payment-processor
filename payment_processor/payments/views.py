from django.http import HttpResponse
from django.shortcuts import render

def payment(request) -> HttpResponse:

    if request.method == "POST":
        pass 
    
    return    