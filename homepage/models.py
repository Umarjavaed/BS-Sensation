from django.db import models
from ckeditor.fields import RichTextField

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to='product_images/')
    hover_image = models.ImageField(upload_to='product_images/', null=True, blank=True)  # New field for hover image

    def __str__(self):
        return self.title
    
class HomepageContent(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField(default="<p>Welcome to the homepage!</p>")  # Default content

    def __str__(self):
        return self.title
    
class Banner(models.Model):
    image = models.ImageField(upload_to='banners/')  # Upload to a 'banners' directory
    alt_text = models.CharField(max_length=255, default="Website Banner")  # Optional: Alt text

    def __str__(self):
        return f"Banner {self.id}"
    
class GaggleText(models.Model):
    quadra_title = models.CharField(max_length=255, help_text="Main title displayed in header")
    sub_quadra_title = models.CharField(max_length=255, help_text="Subtitle displayed under main title")
    narrative_section = models.TextField(help_text="Text content for the about us section")
    delivery_info = models.TextField(help_text="Shipping and delivery information")
    order_instructions = models.TextField(help_text="Order now and contact details")
    
    def __str__(self):
        return f"{self.quadra_title} - {self.sub_quadra_title}"