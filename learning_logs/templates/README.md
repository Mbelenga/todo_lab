### 📝 Note on Template Inheritance

A child template must begin with an `{% extends %}` tag to tell Django which parent template to inherit from. For example:

```django
{% extends "learning_logs/base.html" %}