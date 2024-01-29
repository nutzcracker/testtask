from django.contrib import admin
from .models import Product, Recipe

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	pass

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
	pass
"""
admin.site.register(Product, ProductAdmin)
admin.site.register(Recipe, RecipeAdmin)
"""