from django.shortcuts import render, HttpResponse
from .models import Comment 

# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})    

def events(request):
    return render(request, 'events.html', {})    

def activity(request):
    return render(request, 'activity.html', {})    

def create(request):
    comment = Comment(name='Luis', feedback='Comentario', score=5)
    comment.save() 
    return render(request, 'index.html', {})

def delete(request):
    #comment = Comment.objects.get(id=1)
    #omment.delete()
    Comment.objects.filter(id=2).delete()
    return HttpResponse('Se elimino el objeto')
