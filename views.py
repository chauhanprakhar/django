from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>this is music app home page</h1>")

def detail(request):
    return HttpResponse("<h2>details for album id :" + str(album_id) +"</h2>")
