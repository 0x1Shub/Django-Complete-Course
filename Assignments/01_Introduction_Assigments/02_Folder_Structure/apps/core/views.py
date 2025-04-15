from django.http import JsonResponse
from django.views import View

class MessageView(View):
    def get(self, request):
        return JsonResponse({"message": "GET called"})

    def post(self, request):
        return JsonResponse({"message": "POST called"})
