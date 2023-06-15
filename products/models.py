from typing import Any, Iterable, Optional
from django.db import models
from base.models import BaseModel
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Category(BaseModel):
    name = models.CharField(unique=True,db_column='name',verbose_name=_("Name"),max_length=30)
    
    def __str__(self):
        return self.name
    
    
class SubCategory(BaseModel):
    category = models.ForeignKey(Category,db_column='category_id',verbose_name=_("Category"),on_delete=models.CASCADE)
    name = models.CharField(unique=True,db_column='name',verbose_name=_("Name"),max_length=30)
    
    def __str__(self):
        return self.name
    
    
class Product(BaseModel):
    title = models.CharField(max_length=100,db_column='title',verbose_name=_("Title"))
    description = models.TextField(db_column='description',verbose_name=_("Description"))
    cover_image = models.ImageField(db_column='cover_image',upload_to='products/cover_images')
    category = models.ForeignKey(Category,db_column='category_id',on_delete=models.CASCADE,verbose_name=_("Category"))
    sub_category = models.ForeignKey(SubCategory,db_column='sub_category_id',on_delete=models.CASCADE,verbose_name=_("Sub Category"))
    regular_price = models.PositiveIntegerField(db_column='regular_price',verbose_name=_("Regular Price"))
    discount_price = models.PositiveIntegerField(db_column='discount_price',verbose_name=_("Discount Price"),blank=True,null=True)
    
    
    def __str__(self) -> str:
        return self.title
    
    @property
    def get_price(self):
        return self.discount_price if self.discount_price else self.regular_price
    
    def save(self, *args, **kwargs):
        if self.sub_category.category == self.category:
            super(Product, self).save(*args, **kwargs)
            
            
class ProductImage(BaseModel):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,db_column='product_id',verbose_name=_("Product"))
    image = models.ImageField(db_column='image',upload_to='products/images')
    
    def __str__(self) -> str:
        return self.product.title