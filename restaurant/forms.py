from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.core.validators import (
    RegexValidator,
    MinValueValidator,
    MaxValueValidator,
)

from restaurant.models import Dish, Ingredient


class CookFormMixin(forms.ModelForm):
    years_of_experience = forms.IntegerField(
        required=True,
        validators=[
            MinValueValidator(0, message="Should be between 0 and 50"),
            MaxValueValidator(50, message="Should be between 0 and 50"),
        ],
    )
    username = forms.CharField(
        required=True,
        validators=[
            RegexValidator(
                r"^[A-Za-z0-9_]+$",
                message="Username can contain only latin letters, numbers and '_' sign!",
            )
        ],
    )


class DishForm(forms.ModelForm):
    cooks = forms.ModelMultipleChoiceField(
        queryset=get_user_model().objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Dish
        fields = "__all__"


class IngredientForm(forms.ModelForm):
    dishes = forms.ModelMultipleChoiceField(
        queryset=Dish.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Ingredient
        fields = "__all__"


class CookCreationForm(CookFormMixin, UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "years_of_experience",
        )


class CookExperienceUpdateForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ("years_of_experience",)


class SearchForm(forms.Form):
    search = forms.CharField(
        max_length=100,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search..."}),
    )
