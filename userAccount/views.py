from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from .models import MyUser

class SignForm(View):
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        user_id = request.POST['user_id']
        user_pw = request.POST['user_pw']
        user_email = request.POST['user_email']

        try:
            user_model = MyUser.objects.create(username=user_id, email=user_email)
            user_model.set_password(user_pw)
            user_model.save()
        except:
            return HttpResponse(status=204)

        return HttpResponse(status=200)