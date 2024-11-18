from django.shortcuts import render
from django.views.generic import View
from .models import Info, Service, Hard_skills, school


class HomeItemViews(View):
    def get(self, request):
        context = {
            'info': Info.objects.all(),
            'Services': Service.objects.all(),
            'HardSkills': Hard_skills.objects.all(),
            'School': school.objects.all(),
        }
        return render(request, 'index.html', context)

