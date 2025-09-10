from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    # Meta class to order by name and set plural name
    class Meta:
        ordering = ('name',)
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name
    
class Item(models.Model):
    # Foreign key to Category model, items in category, on cascade (category deleted, items deleted)
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images/', blank=True, null=True)
    isSold = models.BooleanField(default=False)
    # Foreign key to User model,  items by user, on cascade (user deleted, items deleted)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name