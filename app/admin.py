from django.contrib import admin
from .models import Placement, Bid, PlacementBid, Company

# Register your models here.
admin.site.register(Placement)
admin.site.register(PlacementBid)
admin.site.register(Bid)
admin.site.register(Company)