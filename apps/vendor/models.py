from django.db import models
from apps.core.models import User 
from apss.product.models import Product

class Vendor(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.OneToOneField(User, related_name='vendor', on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']
    
    
    def __str__(self):
        return self.name

    def get_posted_tender(self):
        pass 


class CompanyProfile(models.Model):
    SIZE_1_9 = 'size_1-9'
    SIZE_10_49 = 'size_10-49'
    SIZE_50_99 = 'size_50-99'
    SIZE_100 = 'size_100'

    CHOICES_SIZE = (
        (SIZE_1_9, '1-9'),
        (SIZE_10_49, '10-49'),
        (SIZE_50_99, '50-99'),
        (SIZE_100, '100+'),
    )

    ACTIVE = 'active'
    EXPIRED = 'expired'
    ARCHIVED = 'archived'

    CHOICES_STATUS = (
        (ACTIVE, 'Active'),
        (EXPIRED, 'Employed'),
        (ARCHIVED, 'Archived')
    )

    company_name = models.CharField(max_length=255)
    company_address = models.CharField(max_length=255, blank=True, null=True)
    company_zipcode = models.CharField(max_length=255, blank=True, null=True)
    company_place = models.CharField(max_length=255, blank=True, null=True)
    company_country = models.CharField(max_length=255, blank=True, null=True)
    company_size = models.CharField(max_length=20, choices=CHOICES_SIZE, default=SIZE_1_9)

    created_by = models.ForeignKey(User, related_name='tenders', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    changed_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=CHOICES_STATUS, default=ACTIVE)

    def __str__(self):
        return self.company_name

# Model for tender applications
class Application(models.Model):
    tender = models.ForeignKey(Product, related_name='tenders', on_delete=models.CASCADE)
    content = models.TextField()
    experience = models.TextField()

    created_by = models.ForeignKey(User, related_name='tenders', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)