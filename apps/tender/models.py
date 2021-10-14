from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings

from apps.core.models import User 

class Item(models.Model):
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
    
