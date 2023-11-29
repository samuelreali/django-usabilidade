from django.shortcuts import render

# Create your views here.
def home(request):
    template_name ='core/home.html'
    context = {"teste": "teste2"}
    return render(request, template_name, context)