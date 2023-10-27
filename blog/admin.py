from django.contrib import admin
from .models import Profile, Blog

# Register your models here.

admin.site.register([Profile, Blog])
