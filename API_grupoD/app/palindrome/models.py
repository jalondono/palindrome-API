from django.db import models


class Palindromo(models.Model):
    text = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'palindromo'
