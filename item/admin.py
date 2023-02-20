from django.contrib import admin
from item.models import Note, NoteList, Process
# Register your models here.
admin.site.register(Note)
admin.site.register(NoteList)
admin.site.register(Process)