from django.shortcuts import render

def home_page(request):
    return render(request, 'property/home.html', {'user': request.user})

def advertisements_view(request):
    ...