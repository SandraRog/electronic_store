from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.core.exceptions import ValidationError

class Category(models.Model):
    name = models.CharField(max_length=100)
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class Location(models.Model):
    room = models.CharField(max_length=100)
    bookcase = models.CharField(max_length=100)
    shelf = models.CharField(max_length=100)
    cupboard = models.CharField(max_length=100)
    column = models.CharField(max_length=100)
    row = models.CharField(max_length=100)

@receiver(pre_delete, sender=Location)
def prevent_delete_location(sender, instance, **kwargs):
    if instance.part_set.exists():
        raise ValidationError("Nie można usunąć lokalizacji z przypisanymi częściami.")

class Part(models.Model):
    serial_number = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    quantity = models.IntegerField()
    price = models.FloatField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)


@receiver(pre_delete, sender=Category)
def prevent_delete_parent_category(sender, instance, **kwargs):
    if instance.part_set.exists():
        raise ValidationError("Nie można usunąć kategorii z przypisanymi częściami.")

    if instance.parent_category and Category.objects.filter(parent_category=instance.parent_category).exclude(pk=instance.pk).exists():
        raise ValidationError("Nie można usunąć kategorii rodzica, która ma inne podkategorie.")
