from django.contrib import admin
from .  models import TeacherModel
# Register your models here.
# admin.site.register(models.TeacherModel)
@admin.register(TeacherModel)
class TeacherModelAdmin(admin.ModelAdmin):
    list_display = ['id','Name','CourseName','Duration','Seat']