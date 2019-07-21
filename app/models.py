from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.

class Company(models.Model):
    """
    Simply contains company details, referenced by Placement model
    """

    company_name = models.CharField(max_length=255)
    company_address = models.CharField(max_length=255)
    company_description = models.TextField(default="There is currently no description available for this company.")

    company_created = models.DateTimeField(auto_now_add=True)
    company_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name


class Placement(models.Model):
    """
    A placement allows investors to bid on company capital raise
    """

    placement_title = models.CharField(max_length=255)
    placement_slug = models.SlugField()
    placement_company = models.ForeignKey(Company, on_delete=models.CASCADE)


    placement_created = models.DateTimeField(auto_now_add=True)
    placement_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.placement_title


class Bid(models.Model):
    """
    The bid, synonmous with 'order'
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bid_status = models.BooleanField(default=False)

    bid_created = models.DateTimeField(auto_now_add=True)
    bid_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} -{}'.format(self.user, self.bid_status)


class PlacementBid(models.Model):
    """
    The junction table for placement and bid models/tables. Contains every instance of a bid for a placement
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    placement = models.ForeignKey(Placement, on_delete=models.CASCADE)
    bid  = models.ForeignKey(Bid, on_delete=models.CASCADE)
    offer = models.IntegerField()
    shares = models.IntegerField()
    confirmed = models.BooleanField(default=False)
    
    placementbid_created = models.DateTimeField(auto_now_add=True)
    placementbid_modified = models.DateTimeField(auto_now=True)

    class Meta: 
        ordering = ['-placementbid_modified'] 

    def __str__(self):
        return '{} - {} - {}'.format(self.shares, self.offer, self.user)