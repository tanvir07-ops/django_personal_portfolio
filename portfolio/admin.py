from django.contrib import admin
from .models import *

admin.site.site_header = "Tanvir Rifat Admin"
admin.site.site_title = "Tanvir Rifat Admin Area"
admin.site.index_title = "Welcome To The Tanvir Rifat's Area!!!"

# Register your models here.

admin.site.register(Project)
