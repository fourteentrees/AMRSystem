from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, template_name='index.html')

def gpc(request):
    return render(request, template_name='gpc.json', content_type='application/json')

def about(request):
    return render(request, template_name='about.html')