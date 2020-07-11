from django.shortcuts import render, HttpResponse

from .models import User
from django.views.decorators.csrf import csrf_protect
from .forms import UserForm, LoginForm

@csrf_protect
def sign(request):

    user = User()

    username = request.POST.get("username")

    email = request.POST.get("email")

    number = request.POST.get("number")

    name = request.POST.get("name")

    password = request.POST.get("password")


    user.username = username

    user.email = email

    user.phone_number = number

    user.name = name

    user.passsword = password

    user.save()

    request.session['username'] = username

    request.session['email'] = email



    context = {
               'username' : username,
               }
    return HttpResponse(f"Welcome User : {username}")
@csrf_protect
def register(request):

    return render(request, 'templates/Sign.html', {'username' : request.session['username']})


def login(request):

    user = User()

    submitbutton = request.POST.get("submit")

    form = LoginForm(request.POST or None)

    if form.is_valid():

        username_login = form.cleaned_data.get("username")

        password = form.cleaned_data.get("password")

    if user.objects.filter(username=username_login) and user.objects.filter(password=password):

        request.session['username'] = username_login

        content = {
                'username': username_login,
                'form': form,
                'submitbutton': submitbutton,
            }

    return render('templates/Login.html', content)

