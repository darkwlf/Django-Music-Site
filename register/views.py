from django.shortcuts import render, HttpResponse

from .models import User

from .forms import UserForm, LoginForm

def sign(request):

    user = User()

    submitbutton = request.POST.get("submit")

    firstname = ''

    lastname = ''

    emailvalue = ''

    form = UserForm(request.POST or None)

    if form.is_valid():

        username = form.cleaned_data.get("username")

        email = form.cleaned_data.get("email")

        number = form.cleaned_data.get("number")

        name = form.cleaned_data.get("name")

        password = form.cleaned_data.get("password")

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
               'form': form,
               'firstname': firstname,
               'lastname': lastname,
               'submitbutton': submitbutton,
               'emailvalue': emailvalue
               }

    return render(request, 'templates/Sign.html', context)

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

