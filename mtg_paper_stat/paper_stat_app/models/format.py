from django.db import models

class Format(models.Model):
    name = models.fieldsCharfield(max_length=100)