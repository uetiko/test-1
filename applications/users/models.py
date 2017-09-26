from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.db import models


class AdminUser(User):
    username_validator = ASCIIUsernameValidator()

    class Meta:
        proxy = True
        verbose_name = 'Administrador'


class StaffUser(User):
    username_validator = ASCIIUsernameValidator()

    class Meta:
        proxy = True
        verbose_name = 'staff'


class CostomerServiceUser(User):
    username_validator = ASCIIUsernameValidator()

    class Meta:
        proxy = True
        verbose_name = 'Servicio al cliente'


class ClientUser(User):
    username_validator = ASCIIUsernameValidator()

    class Meta:
        proxy = True
        verbose_name = 'Cliente'


class Address(models.Model):
    user = models.ForeignKey(
        ClientUser,
        verbose_name="Cliente",
        related_name="client_relationship_address",
        related_query_name="client_relationship_address",
        on_delete=models.CASCADE
    )
    state = models.CharField(
        verbose_name="Estado",
        max_length=20,
        blank=False,
        null=False
    )
    municipality = models.CharField(
        verbose_name="Municipio/delegación",
        max_length=50,
        blank=False,
        null=False
    )
    suburb = models.CharField(
        verbose_name="Colonia",
        max_length=50,
        blank=False,
        null=False
    )
    street = models.CharField(
        verbose_name="Calle",
        max_length=70,
        blank=False,
        null=False
    )
    outdoor_number = models.IntegerField(
        verbose_name="Numero exterior",
        null=False,
        blank=False,
        default=0
    )
    zipcode = models.IntegerField(
        verbose_name="codigo postal",
        null=False,
        blank=False,
        default=0
    )
