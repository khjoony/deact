from django.db import models

# Create your models here.

from django.urls import reverse
class Sector(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Kospi(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=8)
    owner = models.ForeignKey('Owner', on_delete=models.SET_NULL, null=True)
    sector = models.ManyToManyField(Sector, null=True)
    feature = models.TextField(null=True)

    def display_sector(self):
        return ', '.join([sector.name for sector in self.sector.all()[:3]])

    display_sector.short_description = 'Sector'

    def get_absolute_url(self):
        return reverse('kospi-detail', args=[str(self.id)])
    def __str__(self):
        return self.name

class Kosdak(models.Model):
    name = models.CharField(max_length=20)
    code = models.CharField(max_length=8)
    owner = models.ForeignKey('Owner', on_delete=models.SET_NULL, null=True)
    sector = models.ManyToManyField(Sector, null=True)
    feature = models.TextField(null=True)

    def display_sector(self):
        return ', '.join([sector.name for sector in self.sector.all()[:3]])

    display_sector.short_description = 'Sector'

    def get_absolute_url(self):
        return reverse('kosdak-detail', args=[str(self.id)])

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
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

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
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

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
        help_text='Kosdak user',
    )

    class Meta:
        ordering = ['due_back']
        permissions = (
            ("can_mark_returned", "Set kosdak as returned"),
        )

    def __str__(self):
        return '{0} ({1})'.format(self.id, self.kosdak.name)

class Owner(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('died', null=True, blank=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        return reverse('owner-detail', args=[str(self.id)])

    def __str__(self):
        return '{0}, {1}'.format(self.last_name, self.first_name)
