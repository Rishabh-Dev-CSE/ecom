from django.contrib import admin

from . models import *

admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Billing)
# Register your models here.
