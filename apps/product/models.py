from io import BytesIO
from PIL import Image

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

from apps.core.models import User 



class Product(models.Model):
    tender_no = models.CharField(
        _('tender number'),
        max_length=200,
        null=False,
        blank=False,
        error_messages = {
            "max_length": "The tender NO exceeds max_lenght."
        }
    )
    description = models.TextField(
                _('description'),
                max_length=2000,
                null=True,
                blank=True,
                error_messages ={ 
                    "max_length":"The description is too long. Use a maximum of 2000 characters."
                    } 
                )
    entity_name = models.CharField(
        _('entity'),
        max_length=100,
        null=False,
        blank=False,
        error_messages = {
            "max_length": "The entity name is too long. Use a maximum of 100 characters."
        }
    )
    procurement_method = models.CharField(
                _('procurement method'),
                max_length=200,
                null=True,
                blank=True,
                choices=settings.PROCUREMENT_METHOD,
                error_messages ={ 
                    "max_length":"The hint is too long. Use a maximum of 200 characters."
                    } 
                )
    procurement_category = models.CharField(
        _('procurement category'),
        max_length=150,
        null=True,
        blank=True,
        choices=settings.PROCUREMENT_CATEGORY,
        error_messages = {
            "max_length": "The hint is too long. Use a maximum of 150 characters."
        }
    )
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)
    slug = models.SlugField(max_length=255)
    is_deleted = models.BooleanField(null=False,blank=False,default=False)
    is_rejected = models.BooleanField(default=False)#this remains false until owner rejects report
    is_published = models.BooleanField(default=False)#thisremains false until the owner acknowledges report
    is_active = models.BooleanField(default=False)#this remains false until owner submits the report
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_updated_by = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True,related_name="last_updated_by")
    created_by = models.ForeignKey(User, null=True,blank=True, on_delete=models.CASCADE,related_name="created_by")
    submitted_by = models.ForeignKey(User, null=True,blank=True, on_delete=models.CASCADE,related_name="submitted_by")
    submitted_at = models.DateTimeField(null=True,blank=True)
    closing_date = models.DateTimeField(null=True,blank=True)
    evaluated_by = models.ForeignKey(User, null=True,blank=True, on_delete=models.CASCADE,related_name="evaluated_by")
    deleted_by = models.ForeignKey(User, null=True,blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.tender_no
    
    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return self.thumbnail.url
            else:
                return 'https://via.placeholder.com/240x180.jpg'
    
    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='uploads/', blank=True, null=True)

    def get_thumbnail(self):
        if self.thumbnail:
            return self.thumbnail.url
        else:
            if self.image:
                self.thumbnail = self.make_thumbnail(self.image)
                self.save()

                return self.thumbnail.url
            else:
                return 'https://via.placeholder.com/240x180.jpg'

    def make_thumbnail(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumb_io = BytesIO()
        img.save(thumb_io, 'JPEG', quality=85)

        thumbnail = File(thumb_io, name=image.name)

        return thumbnail
