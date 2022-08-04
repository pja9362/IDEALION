from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, editProfileForm
from .models import CustomUser


#로그인 함수
def login_view(request):

    #로그인 폼에다가 정보 입력 후 제출했을 때 실행됨
    if request.method == 'POST':  
        form = AuthenticationForm(request = request, data = request.POST)
        
        #폼에 들어간 정보가 유효할 때
        if form.is_valid(): 
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request=request, username = username, password = password)
            
            #올바른 아이디/비밀번호를 입력했을 때
            if user is not None: 
                login(request, user)   
                return redirect("home")  #home.html을 화면에 띄워줍니다
        #폼에 들어간 정보가 유효하지 않을 때 or 아이디/비밀번호가 틀렸을 때        
        return render(request, 'login.html', {'form': form})
    
    #로그인 화면에 진입할 때 실행됨
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})


#로그아웃 함수
def logout_view(request):
    logout(request)
    return redirect("home") #로그아웃하고 home.html로 이동


#회원가입 함수
def signup(request):

     #로그인 폼에다가 정보 입력 후 제출했을 때 실행됨
    if request.method == "POST":
        form = RegisterForm(request.POST)

        #폼에 들어간 정보가 유효할 때
        if form.is_valid():
            user = form.save()  #회원 정보를 등록
            login(request,user)  #로그인시켜줌
            return render(request, "selectLocation.html", {'user':user}) #기본위치 설정하는 selectLocation.html로 이동
        
        #폼에 들어간 정보가 유효할 때
        else:
            return render(request, 'signup.html', {'form' : form})  #회원가입 페이지를 다시 띄워줌

    #회원가입 화면에 진입할 때 실행됨
    else:
        form = RegisterForm()
        return render(request, 'signup.html', {'form' : form})

        
#기본 지도 설정 함수
def select(request):

    #위치를 설정하고 전송 버튼을 눌렀을 때 실행되는 함수
    if request.method == "POST":
        user = request.user
        user.lat = request.POST['lat']
        user.lng = request.POST['lng']
        user.save()  #위치 정보를 저장
        return redirect("home")  #home.html로 이동
    
    #기본 지도 설정 화면에 진입할 때 실행됨
    return render(request, "selectLocation.html")  


#회원 정보 수정 함수
def edit_profile(request):

    #정보를 입력하고 전송 버튼을 눌렀을 때 실행되는 함수
    if request.method == "POST":
        form = editProfileForm(request.POST, instance = request.user)
        
        #폼에 들어간 정보가 유효할 때
        if form.is_valid():
            form.save()
            return redirect("home") #정보를 등록하고, home.html로 이동
    
    #회원 정보 수정 화면에 진입할 때 실행되는 함수
    else:
        form = editProfileForm(instance = request.user)
        return render(request, 'edit_profile.html', {'form':form}) 

