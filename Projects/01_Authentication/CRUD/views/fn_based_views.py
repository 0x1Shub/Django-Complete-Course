from django.http import JsonResponse
import json

def get_message(request, message_id):
    if request.method == "GET":
        res = {
            'success': True,
            'content': f"Fetching message with ID: {message_id}"
        }
    else: 
        res = {
            'success': False,
            'content': "Invalid message id"
        }    
    return JsonResponse(res)


def search_messages(request):
    if request.method == "GET": 
        query = request.GET.get('q', '')
        res = {
            'success': True,
            'content': f'Result for query: {query}'
        }

    else:
        res = {
            'success': False,
            'content': "Invalid Request"
        }
    return JsonResponse(res)

def create_message(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        print(body)
        res = {
            'success': True,
            'content': "This is function based view content for create message"
        }
    else :
        res = {
            'success': True,
            'content': "Invalid Request"
        }
    return JsonResponse(res)
    

def update_message(request):
    if request.method == 'PUT':
        res = {
            'success': True,
            'content': "This is function based view content for update message"
        }
    else :
        res = {
            'success': True,
            'content': "Invalid Request"
        }
        
    return JsonResponse(res)

def delete_message(request):
    if request.method == 'DELETE':
        res = {
            'success': True,
            'content': "This is function based view content for delete message"
        }
    else:
        res = {
            'success': False,
            'content': "Invalid Request"
        }

    return JsonResponse(res)


def partial_update_message(request):
    if request.method == 'PATCH':
        body = json.loads(request.body)
        res = {
            'success': True,
            'content': f"Partially updated message with data: {body}"
        }
    else:
        res = {
            'success': False,
            'content': "Invalid Request"
        }

    return JsonResponse(res)