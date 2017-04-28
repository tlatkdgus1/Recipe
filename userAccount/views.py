from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout as _logout
from .models import MyUser

class MainForm(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'main.html')

    def post(self, request, *args, **kwargs):
        pass

class SignForm(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'userAccount/signForm.html')

    def post(self, request, *args, **kwargs):
        user_id = request.POST['user_id']
        user_pw = request.POST['user_pw']

        try:
            user_model = MyUser.objects.create(username=user_id)
            user_model.set_password(user_pw)
            user_model.save()
        except:
            return render(request, 'userAccount/signForm.html', {'error' : "회원가입에 실패하였습니다."})

        return render(request, 'userAccount/loginForm.html', {'msg' : "환영합니다."})

class LoginForm(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'userAccount/loginForm.html')

    def post(self, request, *args, **kwargs):
        user_id = request.POST['user_id']
        user_pw = request.POST['user_pw']
        user = authenticate(username=user_id, password=user_pw)
        if user is not None:
            login(request, user)
            return render(request, 'main.html')
        else:
            return render(request, 'userAccount/loginForm.html', {'msg' : "로그인에 실패하였습니다."})

def logout(request):
    _logout(request)
    return render(request, 'main.html')
