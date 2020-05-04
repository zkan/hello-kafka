from django.db import models


class TextMessage(models.Model):
    message = models.TextField()
