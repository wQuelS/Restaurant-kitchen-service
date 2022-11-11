from django.urls import path

from restaurant.views import index, DishTypeList, DishTypeDetail

urlpatterns = [
    path("", index, name="index"),
    path(
        "dish-type/",
        DishTypeList.as_view(),
        name="dish-type-list",
    ),
    path(
        "dish-type/<int:pk>/",
        DishTypeDetail.as_view(),
        name="dish-type-detail"
    )
]

app_name = "restaurant"
