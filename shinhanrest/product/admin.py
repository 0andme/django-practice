from django.contrib import admin
from .models import Product,Comment,Like
# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # list_display=('name','tstamp')
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    pass