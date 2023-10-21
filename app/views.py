from django.shortcuts import render

def home(request):
    context = {
        "page": "home",
    }

    return render(request, "app/pages/home.html", context)

