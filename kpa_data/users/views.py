from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        phone = data.get('phone')
        password = data.get('password')

        if phone == '7760873976' and password == 'to_share@123':
            return JsonResponse({'token': 'dummy_token_123'}, status=200)
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=401)

    return JsonResponse({'error': 'Method not allowed'}, status=405)
