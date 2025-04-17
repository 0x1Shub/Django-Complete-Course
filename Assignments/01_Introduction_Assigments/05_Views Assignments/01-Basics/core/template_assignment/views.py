from django.shortcuts import render

# Create your views here.
def greet_user(request):
    context = {
        'name': 'Shubham'
    }
    return render(request, 'templates/greet.html', context)
