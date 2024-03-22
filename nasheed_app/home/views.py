from django.shortcuts import render,HttpResponse,redirect
# Create your views here.
from home.models import Contact
from .models import Media
def home(request):
    return render(request, 'index.html')




def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        number=request.POST['number']
        message=request.POST['message']
        # print(name,email,number,message)
        ins=Contact(name=name,email=email,number=number,message=message)
        ins.save()
        # ins.save()
        # print(ins)
    return render(request, 'contact.html')


def video(request):
    # Get all objects from your model
    objects = Media.objects.all()
    context = {'objects': objects}
    return render(request, 'videos.html' , context)

