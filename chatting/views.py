from django.shortcuts import render
from .models import chatting
from django.utils import timezone

def chat(request):
    return render(request, 'chat.html')

def create(request):
    visitor = chatting()
    visitor.chat = request.GET['chat']
    visitor.pub_date = timezone.datetime.now()
    visitor.save()
    return render(request, 'chat.html')

def show(request):
    chats = chatting.objects
    return render(request, 'show.html', {'chats' : chats})