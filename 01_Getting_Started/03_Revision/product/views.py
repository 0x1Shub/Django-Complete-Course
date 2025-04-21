from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello_shubham(request):
    # return HttpResponse('Hello Shubham')
    
    context = {
        "name": "shubham",
        "skills": ['React', 'Django', 'DSA']
    }

    return render(request, 'template.html', {'name': 'John'})

