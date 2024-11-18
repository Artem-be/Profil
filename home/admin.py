from django.contrib import admin
from .models import Info, Service, WebDevelopment, Hard_skills, WebDevelopmentHardSkills, WebDevelopmentSchool, school

class WebDevelopmentInline(admin.TabularInline):
    model = WebDevelopment

class ServiceAdmin(admin.ModelAdmin):
    inlines = (WebDevelopmentInline,)

class WebDevelopmentHardSkillsInLine(admin.TabularInline):
    model = WebDevelopmentHardSkills

class Hard_skillsAdmin(admin.ModelAdmin):
    inlines = (WebDevelopmentHardSkillsInLine,)

class WebDevelopmentSchoolInLine(admin.TabularInline):
    model = WebDevelopmentSchool

class SchoolAdmin(admin.ModelAdmin):
    inlines = (WebDevelopmentSchoolInLine,)

admin.site.register(Service, ServiceAdmin)
admin.site.register(Info)
admin.site.register(Hard_skills, Hard_skillsAdmin)
admin.site.register(school, SchoolAdmin)