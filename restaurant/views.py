from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from restaurant.models import Dish, DishType, Cook


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


class DishTypeListView(generic.ListView):
    model = DishType
    context_object_name = "dish_type_list"
    template_name = "restaurant/dish_type_list.html"
    paginate_by = 5
    queryset = DishType.objects.all()


class DishTypeDetailView(generic.DetailView):
    model = DishType
    context_object_name = "dish_type_list"
    template_name = "restaurant/dish_type_detail.html"
    queryset = DishType.objects.prefetch_related("dish_set").all()


class DishTypeCreateView(generic.CreateView):
    model = DishType
    template_name = "restaurant/dish_type_form.html"
    fields = "__all__"
    success_url = reverse_lazy("restaurant:dish-type-list")


class DishTypeUpdateView(generic.UpdateView):
    model = DishType
    template_name = "restaurant/dish_type_form.html"
    fields = "__all__"
    success_url = reverse_lazy("restaurant:dish-type-list")


class DishTypeDeleteView(generic.DeleteView):
    model = DishType
    success_url = reverse_lazy("restaurant:dish-type-list")
    template_name = "restaurant/dish_type_confirm_delete.html"


class DishListView(generic.ListView):
    model = Dish
    paginate_by = 5
    context_object_name = "dish_list"
    template_name = "restaurant/dish_list.html"
    queryset = Dish.objects.select_related("dish_type")


class DishDetailView(generic.DetailView):
    model = Dish


class CookListView(generic.ListView):
    model = Cook
    paginate_by = 5
    queryset = Cook.objects.all()


class CookDetailView(generic.DetailView):
    model = Cook
    queryset = Cook.objects.prefetch_related("dishes__dish_type")
