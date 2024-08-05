from django.db import models
from models.format import Format

class Archetype(models.Model):
    name = models.fieldsCharfield(max_length=100)
    format = models.ForeignKey(Format, null=False, on_delete=cascade)