from django.contrib import admin
from .models import Product, Category, ProductComment

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ProductCommentAdmin(admin.ModelAdmin):
    """ Allow admin users to manage user comments """
    list_display = (
        'product',
        'product_comment',
        'author',
        'date_added',
    )
    ordering = ['-date_added']


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ProductComment)