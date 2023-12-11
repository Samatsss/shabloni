from django.shortcuts import render

def index(request):
    return render(request, "index.html")
def about(request):
    return render(request, "about.html")

def form(request):
    return render(request, "form.html")

def contacts(request):
    data = {"telefon": "79875881397", "social": "https://vk.com/ss1101"}
    return render(request, "contacts.html", context = data)
