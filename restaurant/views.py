from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from restaurant.models import Dish, DishType, Cook


@login_required
def index(request):
    """View function for the home page of the site."""

    num_dishes = Dish.objects.count()
    num_cooks = Cook.objects.count()
    num_dish_types = DishType.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_cooks": num_cooks,
        "num_dishes": num_dishes,
        "num_dish_types": num_dish_types,
        "num_visits": num_visits + 1,
    }

    return render(request, "restaurant/index.html", context=context)
