from django.shortcuts import render

# Create your views here.

def responsivehome(request):
    context = {}
    return render(request, 'design/responsivehome.html', context)

def responsiveproduct(request):
    context = {}
    return render(request, 'design/responsiveprod.html', context)

def responsivepeople(request):
    context = {}
    return render(request, 'design/responsivepeople.html', context)

def responsivecontact(request):
    context = {}
    return render(request, 'design/responsivecontact.html', context)

