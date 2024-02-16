from django.shortcuts import render

from django.http import JsonResponse

# Comment this for JSON
# def hello_world(request):
#     return JsonResponse({'Message': 'Hello World!'})

#Comment this for HTML
def hello_world(request):
    return render(request, 'hello_world.html')
