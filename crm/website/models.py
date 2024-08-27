from django.db import models

class Record(model.Model):
    created_at = models.DateTimeField(auto_now_add=True)
