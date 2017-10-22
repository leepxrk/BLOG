# coding:utf-8
from django.http import HttpResponse

# Create your views here.

def index(requset):
	return HttpResponse(u"my first Django blog")
