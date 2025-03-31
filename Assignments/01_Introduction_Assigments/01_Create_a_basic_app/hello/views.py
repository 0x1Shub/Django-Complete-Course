from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect

# Create your views here.
def index(request):
    return HttpResponse("Hello, Django!")

# 2. Mutiple View and URL Mapping

def about(request):
    return HttpResponse("This is the About Page")

def contact(request):
    return HttpResponse("Contact us at example@example.com")

# 3. Dynamic URL Parameters
def dynamicURL(request, name):
    return HttpResponse(f"Hello, {name}!")

# 4. Use templates in views
def templateUse(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

# 5. Pass Dynamic Data to Template
def dynamicTemplate(request, first_name):
    template = loader.get_template('index.html')
    context = {'first_name' : first_name}
    return HttpResponse(template.render(context=context))

# 6. Redirecting Views
def home(request):
    return redirect('hello-template')

# 7. Handling 404 Error
def custom_404(request, exception):
    return render(request, '404.html')