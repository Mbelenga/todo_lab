from django.db import models

# Create your models here.

class Topic(models.Model):
    """ A topic the user is learning about """
    text = models.CharFields(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True) # tells Django to automatically set this attribute to the current date and time
whenever the user creates a new topic

def __str__(self):
    """ Returns a string representation of the model """
    return self.text