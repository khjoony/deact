from django.db import models

# Create your models here.
class Kospi(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=8)

    def __str__(self):
        return self.name

class Kosdak(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=8)
    sector = models.TextField(null=True)
    feature = models.TextField(null=True)

    def __str__(self):
        return self.name

import uuid
from datetime import date
from django.contrib.auth.models import User

class KospiInstance(models.Model):
    """Model representing a spedific copy of a stock"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,\
        help_text="Unique ID for this particular stock across whole data" ) 
    kospi = models.ForeignKey('Kospi', on_delete=models.SET_NULL, null=True)
    impirint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False

    OWN_STAUS = (
        ('d', 'Maintenance'),
        ('h', 'Having'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=OWN_STAUS,
        blank=True,
        default='d',
        help_text='Kospi Ownner ',
    )

    class Meta:
        ordering = ['due_back']
        permissions = (
            ("can_mark_returned", "Set kospi as returned"),
        )

    def __str__(self):
        return '{0} ({1})'.format(self.id, self.kospi.name)


class KosdakInstance(models.Model):
    """Model representing a spedific copy of a stock"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,\
        help_text="Unique ID for this particular stock across whole data" ) 
    kosdak = models.ForeignKey('Kosdak', on_delete=models.SET_NULL, null=True, blank=True)
    impirint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False

    OWN_STATUS = (
        ('d', 'Maintenance'),
        ('h', 'Having'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=OWN_STATUS,
        blank=True,
        default='d',
        help_text='Kosdak owner',
    )

    class Meta:
        ordering = ['due_back']
        permissions = (
            ("can_mark_returned", "Set kosdak as returned"),
        )

    def __str__(self):
        return '{0} ({1})'.format(self.id, self.kosdak.name)
