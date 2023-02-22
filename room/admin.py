from django.contrib import admin
from .models import room, roommessage

# Register your models here.
admin.site.register(room)
admin.site.register(roommessage)