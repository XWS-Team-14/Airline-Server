from django.contrib import admin

# Register your models here.
from django.contrib import admin
from airline_server.models import User

@admin.register(User)
class Admin(admin.ModelAdmin):
    pass
