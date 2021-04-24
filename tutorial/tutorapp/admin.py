from django.contrib import admin
from .models import Tutors

class TutorsAdmin(admin.ModelAdmin):
    list_display = ('name', 'disciple')
admin.site.register(Tutors, TutorsAdmin)
# Register your models here.
