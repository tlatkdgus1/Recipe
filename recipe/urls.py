from django.conf.urls import url
from django.contrib import admin
from userAccount import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^main/$', views.MainForm.as_view(), name='main')

]
