from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from restaurant.forms import (
    CookCreationForm,
    CookExperienceUpdateForm,
    DishForm,
)
from restaurant.models import DishType, Dish


class FormsTest(TestCase):
    def setUp(self) -> None:
        self.dish_type = DishType.objects.create(name="test_dish_type")
        self.cook = get_user_model().objects.create_superuser(
            username="cooktest",
            first_name="Test",
            last_name="Testovich",
            password="stronkPass124_",
            years_of_experience=5,
        )
        self.client.force_login(self.cook)

    def test_cook_creation(self):
        form_data = {
            "username": "test_user",
            "password1": "test_pass123",
            "password2": "test_pass123",
            "first_name": "Test first_name",
            "last_name": "Test last_name",
            "years_of_experience": 8,
        }
        form = CookCreationForm(data=form_data)

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

    def test_cook_update(self):
        data = {"years_of_experience": 8}
        form = CookExperienceUpdateForm(data=data)

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, data)

    def test_dish_create(self):
        response = self.client.post(
            reverse("restaurant:dish-create"),
            data={
                "name": "Test model",
                "price": 18.50,
                "dish_type": self.dish_type.id,
                "cooks": self.cook.id,
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Dish.objects.first().name, "Test model")

    def test_dish_delete(self):
        dish = Dish.objects.create(
            name="Test Name",
            dish_type=self.dish_type,
            price=18.00,
        )
        response = self.client.post(
            reverse("restaurant:dish-delete", kwargs={"pk": dish.id})
        )

        self.assertEqual(response.status_code, 302)
        self.assertFalse(Dish.objects.filter(id=dish.id).exists())
