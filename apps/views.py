from cgitb import html
from urllib import request
from rest_framework import viewsets
from apps.serializers import AdminSerializer, BookSerializer
from .models import Book, Admin
from django.shortcuts import render,redirect
from django.contrib import auth
from rest_framework.decorators import action
from apps.forms import Bookfrom


class BookView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # @action(methods=['POST'], url_path='addbook', detail=False)
    def create(self, request, *args, **kwargs):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('/show/')
        else:
            return redirect(f'/add/?error_message={serializer.errors}')


class AdminView(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer

    def create(self, request, *args, **kwargs):
        serializer = AdminSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('/signupsucess/')
        else:
            return redirect('/signupfaild/')



        
    @action(methods=['POST'], url_path='Login', detail=False)
    def login(self, request):
        try:
            admin = Admin.objects.get(username=request.data['username'])
            if admin.password == request.data['password']:
                return redirect('/show/')
            else:
                return redirect('/loginfaild/')

        except Admin.DoesNotExist:
            return redirect('/loginfaild/')

            

    
            

def welcome(request):
    return render(request,'welcome.html')

def signup(request):
    return render(request,'signup.html')

def signup_success(request):
    return render(request,'signup_sucess.html')

def signup_faild(request):
    return render(request,'signupfaild.html')


def login(request):
    return render(request,'login.html')

def show(request):
    books = Book.objects.all()
    return render(request,'show.html', {'data': books})


def loginfaild(request):
    return render(request,'loginfaild.html')


def addbook(request):
    error_message = request.GET.get('error_message')
    if error_message:
        return_dict = {'error_message':error_message}
    else:
        return_dict = {'error_message':''}
    return render(request,'add.html', return_dict)




def delete_book(request,id):
    obj = Book.objects.get(pk=id)
    obj.delete()
    return redirect("/show/")



def update(request,id):
    obj = Book.objects.get(pk = id)
    form = Bookfrom(instance = obj)
    if request.method == "POST":
        form = Bookfrom(request.POST,instance = obj)
        if form.is_valid():
            form.save()
            return redirect("/show/")
    return render(request, 'update.html', {'form': form,'obj':obj})




