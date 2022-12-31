from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# Create your views here.
def register_view(request):
    form = UserCreationForm(request.POST or None)
    
    if form.is_valid():
        user_obj = form.save()
        return redirect("/login")
    context={"form":form
        }
    return render(request,"accounts/register.html",context)


def login_view(request):
    if request.method == "POST":
        #Login via authenticationform
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user = form.get_user()  #get_user method is valid only in AuthenticationForm
            login(request, user)
            return redirect('/')
        else:
            form = AuthenticationForm(request)
        context = {
            "form":form
        }
        return render(request, "accounts/login.html",context)

        # username = request.POST.get("username")
        # password = request.POST.get("password")
        # print(username,password)
        # user = authenticate(request,username=username,password=password)
        # if user is None or password is None:
        #     context = {"error": "Invalid username or password"}
        #     return render(request,"accounts/login.html",context=context)
        # print(user)
        # login(request,user)
        # return redirect('/')


    return render(request,"accounts/login.html",{})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("/login/")
    return render(request,"accounts/logout.html",{})

