from django.contrib import admin
from .models import CustomUser
from contents.models import categoryList

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(categoryList)