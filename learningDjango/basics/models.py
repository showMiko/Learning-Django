from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
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
    

# One to many
class Review(models.Model):
    item=models.ForeignKey(Item, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='user_reviews')
    rating=models.IntegerField()
    comment=models.TextField()
    date_created=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Review for {self.item.name} by {self.user.username}'

# Many to Many
class Tag(models.Model):
    name=models.CharField(max_length=50)
    items=models.ManyToManyField(Item, related_name='tags')

    def __str__(self):
        return self.name 
    
# One to One 
class ItemDetail(models.Model):
    item=models.OneToOneField(Item, on_delete=models.CASCADE, related_name='detail')
    manufacturer=models.CharField(max_length=100)
    warranty_period=models.IntegerField(help_text='Warranty period in months')
    additional_info=models.TextField()

    def __str__(self):
        return f'Details of {self.item.name}'