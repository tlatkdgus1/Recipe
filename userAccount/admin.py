from django.contrib import admin
from .models import *

admin.site.register(MyUser)
admin.site.register(Recipe)
admin.site.register(Tag)
