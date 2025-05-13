from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
from . import forms

def registrar_cosecha(request, id):
    return HttpResponse('hola')

