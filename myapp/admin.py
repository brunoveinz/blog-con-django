from django.contrib import admin
from .models import Project, Taks 

# Register your models here.
#aca registramos lo que queremos que aparezca dentro de admin
admin.site.register(Project)
admin.site.register(Taks)