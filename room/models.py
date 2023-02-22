from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class room(models.Model):
    name = models.TextField(max_length=80)
    code = models.CharField(max_length=8)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name='roomowner', on_delete=models.CASCADE)
    
    members = models.ManyToManyField(User, related_name='room')
    class Meta:
        ordering = ('modified_at',)

class roommessage(models.Model):
    room = models.ForeignKey(room,related_name='message', on_delete=models.CASCADE)
    content = models.TextField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)
    # modified_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name='roomspeaker', on_delete=models.CASCADE)
   