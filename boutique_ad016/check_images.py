import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'boutique_ad016.settings')
django.setup()

from products.models import Product

# Check first product
p = Product.objects.first()
print(f"Sample product: {p.name}")
print(f"Has image field: {bool(p.image)}")
print(f"Has image_url field: {bool(p.image_url)}")
print(f"Image URL value: {p.image_url}")

# Count products with each field
with_image = Product.objects.exclude(image='').count()
with_image_url = Product.objects.exclude(image_url='').exclude(image_url__isnull=True).count()
print(f"\nProducts with image: {with_image}")
print(f"Products with image_url: {with_image_url}")
