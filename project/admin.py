from django.contrib import admin
from box.core.sw_auth.admin import BoxUserAdmin
from project.models import * 



@admin.register(ProjectUser)
class ProjectUserAdmin(BoxUserAdmin):
    search_fields = ['username']


