from django.conf.urls import url
from django.contrib import admin
from userAccount import views
from django.conf.urls import url, include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/$', views.Index.as_view(), name='index'),
    url(r'^user/', include('userAccount.urls', namespace='user')),

]
