from django.contrib import admin

from .models import Project, ProjectStatus, ProjectPermission, ProjectUser

class ProjectStatusInline(admin.TabularInline):

	model = ProjectStatus
	extra = 0
	can_delete = False

class ProjectAdmin(admin.ModelAdmin):
	inlines = [ProjectStatusInline,]

admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectPermission)
admin.site.register(ProjectUser)
