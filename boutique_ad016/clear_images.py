#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'boutique_ad016.settings')
django.setup()

from products.models import Product

# Get all products and clear their image fields
products = Product.objects.all()
count = 0

for product in products:
    if product.image:
        product.image.delete()  # Delete the actual file from S3
        product.image = None    # Clear the field
    
    if product.image_url:
        product.image_url = None  # Clear external URL field
    
    if product.image or product.image_url:
        product.save()
        count += 1

print(f"Cleared images from {count} products")
