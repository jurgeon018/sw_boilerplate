from django.shortcuts import render
from sw_utils.sw_content.models import Page 


def index(request):
    page = Page.objects.get(code=index)
    return render(request, 'project/index.html', locals())



