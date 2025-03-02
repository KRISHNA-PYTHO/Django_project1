from django.db import models
from base.models import basemodel

class category(basemodel):
    category_name=models.CharField(max_length=100)
    slug =models.SlugField(unique=True,null=True ,blank=True)
    category_image=models.ImageField(upload='categories')

class product(basemodel):
    product_name=models.CharField(max_length=100)
    slug =models.SlugField(unique=True,null=True ,blank=True)
    category= models.ForeignKey(category,ondelete=models.CASCADE,related_name="products")
    price=models.IntegerField()
    product_description=models.TextField()
    
class productimage(basemodel):
    product=models.ForeignKey(product,on_delete=models.CASCADE,related_name="product_images")
    image=models.ImageField(upload="product")