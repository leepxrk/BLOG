# coding:utf-8
from django.http import HttpResponse

# Create your views here.

def index(requset):
	return HttpResponse(u"<H1>my first Django blog</h1>")
	

