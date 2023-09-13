from django.db import models

# Create your models here.
class Event(models.Model):
    event_title = models.CharField(max_length=120)
    location = models.CharField(max_length=70)
    date  = models.CharField(max_length=120)
    desc = models.TextField()

    def __str__(self):
        return self.event_title


class Applicant(models.Model):
    fname = models.CharField(max_length=120)
    lname = models.CharField(max_length=120)
    mailid = models.CharField(max_length=70)
    phone = models.PositiveBigIntegerField()
    event = models.ForeignKey('Event',on_delete=models.CASCADE)

    def __str__(self):
        return self.fname + " " + self.lname