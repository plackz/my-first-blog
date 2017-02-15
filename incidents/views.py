from django.shortcuts import render

# Create your views here.
def ncr(request):
    return render(request, 'admin/incidents/')
