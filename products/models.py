from django.db import models
from django.contrib.auth.models import User


STATUS = ((0, 'Draft'), (1, 'Published'))

class Post(models.Model):
    CATEGORY_CHOICES = (
        ('gym', 'classes'),
    )
    title = models.CharField(max_length=210, unique=True)
    slug = models.SlugField(max_length=210, unique=True)
    excerpt = models.TextField(blank=True)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True, blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

class Product(models.Model):
    category = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    # Other product-related fields
    
    def __str__(self):
        return self.name

class NutritionPlan(models.Model):
    category = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return self.title




