from django.shortcuts import render
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout as _logout
from .models import MyUser

class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

    def post(self, request, *args, **kwargs):
        pass

class Account(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'account.html')

    def post(self, request, *args, **kwargs):
        pass

class SignForm(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'userAccount/signForm.html')

    def post(self, request, *args, **kwargs):
        user_id = request.POST['user_id']
        user_pw = request.POST['user_pw']
        user_pwConfirm = request.POST['user_pwConfirm']
        user_nickname = request.POST['user_nickname']

        if(user_pw == user_pwConfirm):
            try:
                user_model = MyUser.objects.create(username=user_id, nickname=user_nickname)
                user_model.set_password(user_pw)
                user_model.save()
            except:
                return render(request, 'account.html', {'msg' : "회원가입에 실패하였습니다."})

            return render(request, 'index.html', {'msg' : "환영합니다."})

        else:
            return render(request, 'account.html', {'msg': "비밀번호가 다릅니다."})

class LoginForm(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'account.html')

    def post(self, request, *args, **kwargs):
        user_id = request.POST['user_id']
        user_pw = request.POST['user_pw']

        user = authenticate(username=user_id, password=user_pw)
        if user is not None:
            login(request, user)
            return render(request, 'index.html')
        else:
            return render(request, 'account.html', {'msg' : "로그인에 실패하였습니다."})

def logout(request):
    _logout(request)
    return render(request, 'index.html')
