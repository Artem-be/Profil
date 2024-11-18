from django.db import models

class Info(models.Model):
    full_name = models.CharField(max_length=128, unique=True)
    number = models.CharField(max_length=128, unique=True)
    email = models.EmailField()
    info = models.TextField()

    def __str__(self):
        return f"My info:{self.full_name}"

class WebDevelopment(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    service = models.ForeignKey('Service', on_delete=models.CASCADE)

class Service(models.Model):
    title = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.title}"

class WebDevelopmentHardSkills(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    Hard_skills = models.ForeignKey('Hard_skills', on_delete=models.CASCADE)

class Hard_skills(models.Model):
    title = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.title}"

class WebDevelopmentSchool(models.Model):
    title = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    description = models.TextField()
    school = models.ForeignKey('school', on_delete=models.CASCADE)

class school(models.Model):
    title = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.title}"

