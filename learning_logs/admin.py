from django.contrib import admin

from .models import Topic, Entry
"""
The dot in front of models tells Django
to look for models.py in the same directory as admin.py. 
"""

admin.site.register(Topic)
admin.site.register(Entry)
"""
This code admin.site.register() tells Django to manage our model
through the admin site.
"""