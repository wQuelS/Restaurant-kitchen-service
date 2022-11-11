from django.urls import path

from restaurant.views import index, DishTypeListView, DishTypeDetailView, DishListView, DishDetailView, CookListView, \
    CookDetailView, DishTypeCreateView, DishTypeUpdateView, DishTypeDeleteView

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
        name="dish-type-detail",
    ),
    path(
        "categories/create/",
        DishTypeCreateView.as_view(),
        name="dish-type-create",
    ),
    path(
        "categories/<int:pk>/update",
        DishTypeUpdateView.as_view(),
        name="dish-type-update",
    ),
    path(
        "categories/<int:pk>/delete",
        DishTypeDeleteView.as_view(),
        name="dish-type-delete",
    ),
    path(
        "dishes/",
        DishListView.as_view(),
        name="dish-list",
    ),
    path(
        "dishes/<int:pk>/",
        DishDetailView.as_view(),
        name="dish-detail",
    ),
    path(
        "cooks/",
        CookListView.as_view(),
        name="cook-list",
    ),
    path(
        "cooks/<int:pk>/",
        CookDetailView.as_view(),
        name="cook-detail",
    ),
]

app_name = "restaurant"
