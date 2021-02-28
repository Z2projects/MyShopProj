from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.http import HttpResponse

# Create your views here.
def register(request):
    if request.method == 'POST':
            fn = request.POST['first_name']
            ln = request.POST['last_name']
            un = request.POST['username']
            pw1 = request.POST['password1']
            pw2 = request.POST['password2']
            if pw1 == pw2:
                if User.objects.filter(username=un).exists():
                    return HttpResponse("user already exist")
                else:
                    user = User.objects.create_user(username=un,password=pw1,first_name=fn,last_name=ln)
                    user.save()
                    return redirect("/retail")
            else:
                return HttpResponse("password did not match")
    else:
        return render(request,'register.html')
            
def login(request):
    if request.method=='POST':
        un = request.POST['username']
        pw = request.POST['password']  
        user = auth.authenticate(username=un,password=pw) 
        if user is not None:
            auth.login(request, user)
            return redirect('/retail')
        else:
            return HttpResponse("invalid user or password")
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
        
