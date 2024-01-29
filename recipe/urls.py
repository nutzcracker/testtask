from django.urls import path
from .views import add_product, count, noproduct


urlpatterns = [
    path('add_product_to_recipe/', add_product),
    path('cook_recipe/', count),
    path('show_recipes_without_product/', noproduct),
]