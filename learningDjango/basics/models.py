from django.db import models
from django.utils import timezone
# Create your models here.
class Item(models.Model):

    TYPE_CHOICES = [
        ('T1', 'Type 1'),
        ('T2', 'Type 2'),
        ('T3', 'Type 3'),
        ('T4', 'Type 4'),
        ('T5', 'Type 5'),
    ]

    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='items/')
    date_added=models.DateTimeField(default=timezone.now)
    type=models.CharField(max_length=2, choices=TYPE_CHOICES, default='T1')
    description=models.TextField()
    price=models.DecimalField(max_digits=10, decimal_places=2)
    in_stock=models.BooleanField(default=True)
    
    def __str__(self):
        return self.name