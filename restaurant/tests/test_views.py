from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from restaurant.models import DishType, Dish, Cook

DISH_TYPE_LIST_URL = reverse("restaurant:dish-type-list")
DISH_LIST_URL = reverse("restaurant:dish-list")
COOK_CREATE = reverse("restaurant:cook-create")


class PublicDishTypeTest(TestCase):
    def test_login_required(self):
        response = self.client.get(DISH_TYPE_LIST_URL)

        self.assertNotEqual(response.status_code, 200)


class PrivateDishTypeTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user("Test", "Pass11243fd")
        self.client.force_login(self.user)

    def test_pagination_is_five(self):
        number_of_dish_types = 10
        for dish_type_id in range(number_of_dish_types):
            DishType.objects.create(
                name=f"Toyota {dish_type_id}",
            )

        response = self.client.get(DISH_TYPE_LIST_URL)
        self.assertTrue("is_paginated" in response.context)
        self.assertTrue(response.context["is_paginated"] is True)
        self.assertEqual(len(response.context["dish_type_list"]), 5)

    def test_retrieve_dish_type_list(self):
        DishType.objects.create(name="Audi")

        response = self.client.get(DISH_TYPE_LIST_URL)
        dish_type = DishType.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["dish_type_list"]), list(dish_type)
        )

    def test_correct_template_used(self):
        response = self.client.get(DISH_TYPE_LIST_URL)
        self.assertTemplateUsed(response, "restaurant/dish_type_list.html")


class PublicDishTest(TestCase):
    def test_login_required(self):
        response = self.client.get(DISH_LIST_URL)

        self.assertNotEqual(response.status_code, 200)


class PrivateDishTest(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username="testName",
            password="tEst12345_",
        )
        self.client.force_login(self.user)

    def test_dish_list_private(self):
        dish_type = DishType.objects.create(
            name="Testtt",
        )
        Dish.objects.create(name="TestName", dish_type=dish_type, price=18.80)

        response = self.client.get(DISH_LIST_URL)
        dishes = Dish.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["dish_list"]), list(dishes))

    def test_correct_template_used(self):
        response = self.client.get(DISH_LIST_URL)
        self.assertTemplateUsed(response, "restaurant/dish_list.html")


class PublicCookTests(TestCase):
    def test_login_required(self):
        response = self.client.get(COOK_CREATE)

        self.assertEqual(response.status_code, 200)


class PrivateCookTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create(
            username="teststetadf", password="asdfasdfasdf"
        )
        self.client.force_login(self.user)

    def test_retrieve_cook_info(self):
        response = self.client.get(reverse("restaurant:cook-list"))
        cook = Cook.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context["cook_list"]), list(cook))
        self.assertTemplateUsed(response, "restaurant/cook_list.html")

    def test_create_cook(self):
        form_data = {
            "username": "test123",
            "password1": "Stronkpas4",
            "password2": "Stronkpas4",
            "years_of_experience": 7,
            "first_name": "TestName",
            "last_name": "TestSurname",
        }
        self.client.post(reverse("restaurant:cook-create"), data=form_data)
        new_user = get_user_model().objects.get(username=form_data["username"])

        self.assertEqual(new_user.first_name, form_data["first_name"])
        self.assertEqual(new_user.last_name, form_data["last_name"])
        self.assertEqual(
            new_user.years_of_experience, form_data["years_of_experience"]
        )
