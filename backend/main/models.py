from django.db import models

class Users(models.Model):
    class Meta:
        verbose_name_plural = "Organisation Users"
    organisation_code = models.CharField(unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=128)


class Events(models.Model):
    class Meta:
        verbose_name_plural = "Events"
        
    organisation_code = models.CharField()
    event_name = models.CharField(max_length=255)
    event_data = models.CharField()

class Faculty_Advisors(models.Model):
    class Meta:
        verbose_name_plural = "Faculty_Advisors"
    
    organisation_code = models.CharField()
    name = models.CharField()
    email = models.CharField(unique=True)
    password = models.CharField()


class Certificates(models.Model):
    class Meta:
        verbose_name_plural = "Certificates"
        unique_together = (('organisation_code', 'event_name', 'participant_email'),)
    
    faculty_advisor = models.CharField()
    organisation_code = models.CharField()
    event_name = models.CharField()
    participant_email = models.CharField()
    status = models.CharField()