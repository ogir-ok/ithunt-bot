from django.db import models


class Vacancy(models.Model):
    text = models.TextField()