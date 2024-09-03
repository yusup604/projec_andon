import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt

# Global variable to keep the status
status = "off"

def index(request):
    return render(request, 'index.html')

def leader(request):
    return render(request, 'leader.html')

def status_leader(request):
    return render(request, 'status_leader.html', {'status': status})

@csrf_exempt
def update_status(request):
    global status
    if request.method == 'POST':
        status = "leader"  # Set status to 'leader' to activate the blinking box
        html = render_to_string('status_leader.html', {'status': status})
        return HttpResponse(html)
    return HttpResponse(status=400)

@csrf_exempt
def reset_status(request):
    global status
    if request.method == 'POST':
        status = "off"
        html = render_to_string('status_leader.html', {'status': status})
        return HttpResponse(html)
    return HttpResponse(status=400)

def display(request):
    return render(request, 'display.html')

@csrf_exempt
def update_display_status(request):
    global status
    if request.method == 'POST':
        data = json.loads(request.body)
        status = data.get('status', 'off')
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)

def fetch_display_status(request):
    global status
    return JsonResponse({'status': status})

@csrf_exempt
def reset_display_status(request):
    global status
    if request.method == 'POST':
        status = "reset"
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)

def perbaikan(request):
    return render(request, 'perbaikan.html')
