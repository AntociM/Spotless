from django.shortcuts import render



def home_page_view(request):
    context = {}
    return render(request, "index.html", context)

