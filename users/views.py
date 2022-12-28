from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required, permission_required

def index(request):
    return render(request, 'users/index.html')

def signup2(request):
    return render(request, 'users/signup2.html')

def signup(request):
    return render(request, 'users/signup.html')

def choose(request):
    return render(request, 'users/choose.html')

def loginview(request):
    return render(request, 'users/login.html')

def home(request):
    user_list = User.objects.order_by('-pub_date')[:5]
    context = {'user_list': user_list}
    return render(request, 'users/home.html', context )


def processadd(request):
    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    middlei = request.POST.get('middlei')
    username = request.POST.get('username')
    password = request.POST.get('password')
    email = request.POST.get('email')
    pnumber = request.POST.get('pnumber')
    user_type = request.POST.get('user_type')

    if request.FILES.get('image'):
        user_pic = request.FILES.get('image')
    else:
        user_pic = 'profile_pic/image.png'
    
    try:
        n = User.objects.get(user_email = email)
        return render(request, 'users/signup.html', {
            'error_message': "Duplicated email : " + email 
        })
    except ObjectDoesNotExist:
        user = User.objects.create(user_email = email, user_fname = fname, user_lname = lname, 
        user_initial = middlei, username = username, password = password, user_pnumber = pnumber, user_image = user_pic, user_type = user_type)
        user.save()
        return HttpResponseRedirect('loginview')

def detail(request, profiletab):
    try:
        user = User.objects.get(pk=profiletab)
    except User.DoesNotExist:
        raise Http404('Profile does not exist')
    return render(request, 'users/detail.html', {'user': user })

def process(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username=username,  password=password)
    if user is not None:
            
            login(request, user)
            return HttpResponseRedirect('/users/home')
    else:
            return render(request, 'users/login.html', {
                'error_message' : 'Login Failed'
        })
    
def processlogout(request):
    logout(request)
    return HttpResponseRedirect('/loginview')
 
    

