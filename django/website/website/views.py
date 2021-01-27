from django.http import HttpResponse
def hello(request):
    return HttpResponse("<h1> Hello django</h1>")

def greet(request):
    user=request.GET['user']
    return HttpResponse(f"<h1>Hello {user} <h1/>")
    



















