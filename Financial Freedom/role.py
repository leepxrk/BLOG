from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def add(request):
    a = request.GET.get('a',0)
    b = request.GET.get('b',0)
    c = int(a) + int(b)
    return HttpResponse(str(c))

# request.GET 类似字典，因此这里用 request.GET.get('a',0)，当没有传递a的时候，将a默认为0