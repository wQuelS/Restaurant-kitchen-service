from django.urls import path

from restaurant.views import index, DishTypeListView, DishTypeDetailView, DishListView, DishDetailView

urlpatterns = [
    path("", index, name="index"),
    path(
        "categories/",
        DishTypeListView.as_view(),
        name="dish-type-list",
    ),
    path(
        "categories/<int:pk>/",
        DishTypeDetailView.as_view(),
        name="dish-type-detail"
    ),
    path(
        "dishes/",
        DishListView.as_view(),
        name="dish-list"
    ),
    path(
        "dishes/<int:pk>/",
        DishDetailView.as_view(),
        name="dish-detail"
    ),
]

app_name = "restaurant"
