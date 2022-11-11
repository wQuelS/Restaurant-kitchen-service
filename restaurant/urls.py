from django.urls import path

from restaurant.views import index, DishTypeListView, DishTypeDetailView, DishListView

urlpatterns = [
    path("", index, name="index"),
    path(
        "dish-type/",
        DishTypeListView.as_view(),
        name="dish-type-list",
    ),
    path(
        "dish-type/<int:pk>/",
        DishTypeDetailView.as_view(),
        name="dish-type-detail"
    ),
    path(
        "dish-list/",
        DishListView.as_view(),
        name="dish-list"
    ),
]

app_name = "restaurant"
