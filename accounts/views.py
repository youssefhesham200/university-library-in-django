from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .models import User, FormBook
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .form import StudentSignUpForm, OwnerSignUpForm, AddForm,ChangeUser,Addextend

# Create your views here.
def index(request) :
    return render(request, 'signUp/index.html')


def register(request) :
    return render(request, 'signUp/register.html')


class StudentRegister(CreateView) :
    model = User
    form_class = StudentSignUpForm
    template_name = 'signUp/StudentRegister.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('booksstudent')


class OwnerRegister(CreateView) :
    model = User
    form_class = OwnerSignUpForm
    template_name = 'signUp/OwnerRegister.html'

    def form_valid(self, form) :
        user = form.save()
        login(self.request, user)
        return redirect('booksadmin')


def login_request(request) :
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_owner is True:
                login(request, user)
                return redirect('booksadmin')
            elif user is not None and user.is_student is True :
                login(request, user)
                return redirect('booksstudent')
            else :
                messages.error(request, "Invalid username or password")
        else :
            messages.error(request, "Invalid username or password")
    return render(request, 'signUp/login.html',
                  context={'loginform' : AuthenticationForm()})


def logout_view(request):
    logout(request)
    return redirect('index')


def addBook(request):
    if request.method == 'POST':
        myform = AddForm(request.POST)
        myform.save()
    return render(request, 'pages/AddBook.html', {'myform' : AddForm})


def booksadmin(request):
    book = FormBook.objects.all()
    name = None
    if 'searchName' in request.GET:
        name = request.GET['searchName']
        if name:
            book = book.filter(bookName__icontains=name)

    return render(request, 'pages/booksadmin.html', {'book': book})


def booksstudent(request):
    book = FormBook.objects.all()
    name = None
    if 'searchName' in request.GET:
        name = request.GET['searchName']
        if name:
            book = book.filter(bookName__icontains=name)

    return render(request, 'pages/booksStudent.html', {'book': book})


def updateBook(request, id):
    bookid = FormBook.objects.get(id=id)
    if request.method == 'POST':
        booksave = AddForm(request.POST, request.FILES, instance=bookid)
        if booksave.is_valid():
            booksave.save()
    else:
        booksave = AddForm(instance=bookid)
    context = {
        'form': booksave,
    }
    return render(request, 'pages/updateBook.html', context)


def updateUser(request):
    if request.method == 'POST':
        usersave = ChangeUser(request.POST, request.FILES, instance=request.user)
        if usersave.is_valid():
            usersave.save()
    else:
        usersave = ChangeUser(instance=request.user)
    context = {
        'form': usersave
    }
    return render(request, 'pages/updateUser.html', context)


def updateStudent(request):
    if request.method == 'POST':
        usersave = ChangeUser(request.POST, request.FILES, instance=request.user)
        if usersave.is_valid():
            usersave.save()
    else:
        usersave = ChangeUser(instance=request.user)
    context = {
        'form': usersave
    }
    return render(request, 'pages/updateStudent.html', context)


def borrowing(request, id):
    bookid = FormBook.objects.get(id=id)
    bookid.status = 'borrowed'
    bookid.returning = 7
    bookid.save(update_fields=['status'])
    bookid.save(update_fields=['returning'])
    return redirect('booksstudent')


def returning(request, id):
    bookid = FormBook.objects.get(id=id)
    bookid.status = 'available'
    bookid.returning = 0
    bookid.save(update_fields=['status'])
    bookid.save(update_fields=['returning'])
    return redirect('booksstudent')


def extend(request, id):
    bookid = FormBook.objects.get(id=id)
    if request.method == 'POST':
        booksave = Addextend(request.POST, request.FILES, instance=bookid)
        if booksave.is_valid():
            booksave.save()
    else:
        booksave = Addextend(instance=bookid)
    context = {
        'form': booksave,
    }
    return render(request, 'pages/extend.html', context)
