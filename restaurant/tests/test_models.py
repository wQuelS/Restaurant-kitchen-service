from django.contrib.auth import get_user_model
from django.test import TestCase

from restaurant.models import DishType, Dish, Ingredient


class ModelsTests(TestCase):
    def test_dish_type_str(self):
        dish_type = DishType.objects.create(
            name="TestName"
        )
        self.assertEqual(
            str(dish_type), dish_type.name
        )

    def test_cook_str(self):
        cook = get_user_model().objects.create_user(
            username="TestUsername",
            password="TestPass",
            first_name="TestName",
            last_name="TestSurname",
        )

        self.assertEqual(
            str(cook),
            f"{cook.first_name} {cook.last_name}",
        )

    def test_cook_experience(self):
        username = "TestUsername"
        password = "TestPassword"
        years_of_experience = 8
        cook = get_user_model().objects.create_user(
            username=username, password=password, years_of_experience=years_of_experience
        )

        self.assertEqual(cook.username, username)
        self.assertTrue(cook.check_password(password))
        self.assertEqual(cook.years_of_experience, years_of_experience)

    def test_dish_str(self):
        dish_type = DishType.objects.create(
            name="TestName"
        )
        dish = Dish.objects.create(name="TestModel", dish_type=dish_type, price=18.88)

        self.assertEqual(str(dish), dish.name)

    def test_ingredient_str(self):
        ingredient = Ingredient.objects.create(name="test-test")

        self.assertEqual(str(ingredient), ingredient.name)