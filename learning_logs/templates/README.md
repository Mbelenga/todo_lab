📝 Note on Template Inheritance
A child template must begin with an {% extends %} tag to tell Django which parent template to inherit from. For example:

django
Copy
Edit
{% extends "learning_logs/base.html" %}
This line pulls in everything from the base.html file and allows the child template (e.g. index.html) to insert custom content in specific blocks—like {% block content %}—defined in the base template.

Using this approach keeps your templates organized and allows for consistent structure across pages while focusing on what's unique to each one.