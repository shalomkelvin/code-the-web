from django.shortcuts import render
from travel_abroad.forms import UserForm, UserprofileInfoForm

#imports for login and logout
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.

def index(request):
    return render(request, 'travel_abroad/index.html')



#logout views
@login_required
def user_logout(request):
    logout(request)
    return render(request, 'travel_abroad/index.html')





def register(request):

    registered = False

    if request.method == "post":

        user_form = UserForm(data=request.POST)
        profile_form = UserprofileInfoForm(data = request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            proflie.user = username

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserprofileInfoForm()

    return render(request, 'travel_abroad/registration.html', {'user_form':user_form, 'profile_form':profile_form
                                                                              , 'registerd':registered

          })

# coding the login

def user_login(request):

     if request.method == 'POST':
         username = request.POST.get('username')
         password = request.POST.get('password')

         user = authenticate(username=username, password=password)

         if user:
             if user.is_active:
                 login(request, user)
                 return HttpResponseRedirect(reverse('index'))

             else:
                return HttpResponse('ACCOUNT NOT ACTIVE')

         else:
            print("Someone tried to login!")
            print('Username: {} and password {}'.format(username,password))
            return HttpResponse("NOT A VALID ACCOUNT")

     else:
        return render(request, 'travel_abroad/login.html', {})
