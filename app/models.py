from django.db import models
from django.conf import settings

# Create your models here.

class Company(models.Model):
    """
    Simply contains company details
    """

    company_name = models.CharField(max_length=255)
    company_address = models.CharField(max_length=255)
    company_description = models.TextField(default="There is currently no description available for this company.")

    company_created = models.DateTimeField(auto_now_add=True)
    company_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name


class PlacementBid(models.Model):
    """
    The junction table for placement and bid models/tables. Contains every instance of a bid for a placement
    """

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    placementbid_created = models.DateTimeField(auto_now_add=True)
    placementbid_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.


class Placement(models.Model):
    """
    A placement allows a group of investors to bid on company capital raise
    """
    placement_company = models.ForeignKey(Company, on_delete=models.CASCADE)

    placement_created = models.DateTimeField(auto_now_add=True)
    placement_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.


class Bid(models.Model):

    bid_amount = models.IntegerField()
    bid_shares = models.IntegerField()

    bid_created = models.DateTimeField(auto_now_add=True)
    bid_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.