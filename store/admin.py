from django.contrib import admin
from .models import Product, Catagory, Customer , Order , Contact

# Register your models here.

admin.site.register(Product)
admin.site.register(Catagory)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Contact)
