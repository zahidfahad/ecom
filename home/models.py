from django.db import models
from base.models import BaseModel
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Banner(BaseModel):
    title = models.CharField(max_length=50,db_column='title',verbose_name=_("Title"),null=True,blank=True)
    description = models.TextField(db_column='description',verbose_name=_("Description"),null=True,blank=True)
    image = models.ImageField(db_column='image',upload_to='banners',verbose_name=_("Banner Image"))