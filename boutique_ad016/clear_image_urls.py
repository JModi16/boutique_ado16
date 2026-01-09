#!/usr/bin/env python
import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'boutique_ad016.settings')

# Setup Django
sys.path.insert(0, '/app/boutique_ad016')
django.setup()

from products.models import Product

# Clear all image_url values
Product.objects.all().update(image_url='')
print("All image_url values cleared!")
