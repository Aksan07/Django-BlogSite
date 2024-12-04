from django.shortcuts import render

# Create your views here.
def starting_page(request):
    return render(request,"BlogApp/index.html")
def posts(request):
    pass
def post_details(request):
    pass