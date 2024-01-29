from django.shortcuts import render
from .models import Recipe, Product
from django.db import transaction
from django.http import HttpResponse


@transaction.atomic
def add_product(request):
    recipe_id = request.GET.get('recipe_id')
    try:
        recipe = Recipe.objects.select_for_update().get(id=recipe_id)
        product_id = request.GET.get('product_id')
        weight = request.GET.get('weight')
        recipe.products[product_id]['weight'] = weight
        recipe.save()
    except:
        return HttpResponse("Recipe id does not exist")


@transaction.atomic
def count(request):
    try:
        recipe_id = request.GET.get('recipe_id')
        recipe = Recipe.objects.select_for_update().get(id=recipe_id)
        for product_id in recipe.products:
            product = Product.objects.select_for_update().get(id=product_id)
            product.count += 1
            product.save()
    except:
        return HttpResponse("Recipe id does not exist")


@transaction.atomic
def noproduct(request):
    recipe_list = {}
    product_id = request.GET.get('product_id')
    recipes_all = Recipe.objects.select_for_update().all()
    recipes = recipes_all.filter(products__has_key=product_id)
    recipes_no_product = recipes_all.exclude(products__has_key=product_id)

    if recipes_all.filter(products__has_key=product_id).exists():

        for recipe in recipes:
            if int(recipe.products[product_id]['weight']) < 10:
                recipe_list[recipe.id] = recipe.name

        for recipe_no_product in recipes_no_product:
            recipe_list[recipe_no_product.id] = recipe_no_product.name

    context = {
        "recipe_list": recipe_list
    }

    return render(request, "index.html", context)
