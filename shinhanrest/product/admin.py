from django.contrib import admin
from .models import Product,Comment
# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # list_display=('name','tstamp')
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
