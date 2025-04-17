from django.http import HttpResponse

def hello_shubham(request):
    print("✅ View triggered")
    return HttpResponse("Hello Shubham !!!")
