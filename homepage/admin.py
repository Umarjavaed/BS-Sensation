# homepage/admin.py
from .models import GaggleText
from django.contrib import admin
from .models import Product
from .models import HomepageContent
from ckeditor.widgets import CKEditorWidget
from django import forms
from .models import Banner

admin.site.site_header = "BS Sensation"  # Change the browser tab title
admin.site.site_title = "BS Sensation Admin Portal"  # Change the browser tab title
admin.site.index_title = "Welcome to BS Sensation Administration"  # Change the main index title

class HomepageContentForm(forms.ModelForm):
    class Meta:
        model = HomepageContent
        fields = ['title', 'content']
        widgets = {
            'content': CKEditorWidget(),
        }

class HomepageContentAdmin(admin.ModelAdmin):
    form = HomepageContentForm


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'discount', 'image', 'hover_image')  # remove 'discount_price' or correct the field

class GaggleTextAdmin(admin.ModelAdmin):
    list_display = ('quadra_title', 'sub_quadra_title')  # Display these fields in the admin list view

admin.site.register(GaggleText, GaggleTextAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(HomepageContent, HomepageContentAdmin)
admin.site.register(Banner)
