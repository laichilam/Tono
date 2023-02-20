from django.db import models

# Create your models here.
class NoteList(models.Model):
    name = models.TextField(max_length=30)
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now_add=True)
   
    class meta:
        ordering = ('name')

    def __str__(self):
       return self.name

class Note(models.Model):
    name = models.TextField(max_length=30)
    detail = models.TextField(max_length=80)
    inlist = models.ForeignKey(NoteList,related_name='notes',on_delete=models.CASCADE)
    complete = models.BooleanField(default=False)
    priority = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ('priority')
        
    def __str__(self):
       return self.name

class Process(models.Model):
    name = models.TextField(max_length=30)
    innote = models.ForeignKey(Note,related_name='processes',on_delete=models.CASCADE)
    detail = models.TextField(max_length=80)
    
    created_at = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ('name')
        
    def __str__(self):
       return self.name
    