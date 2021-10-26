from django.db import models

# Create your models here.
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Contact(models.Model):
    name = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255, blank=True)
    telephone = models.CharField(max_length=255)
    email = models.EmailField()
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    enable = models.BooleanField(default=True)
    rate = models.DecimalField(max_digits=2, decimal_places=1)
    category = models.ForeignKey(Category, related_name="contacts", on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
        unique_together = ['name', 'category']
        ordering = ['-name']

    def __str__(self):
        return f'contact {self.name}/{self.category} rated as {self.rate}'
