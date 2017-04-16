from django.contrib import admin

from .models import Project,ProjectStatus

class ProjectStatusInline(admin.TabularInline):

	model = ProjectStatus
	extra = 0
	can_delete = False

class ProjectAdmin(admin.ModelAdmin):
	inlines = [ProjectStatusInline,]

admin.site.register(Project, ProjectAdmin)
