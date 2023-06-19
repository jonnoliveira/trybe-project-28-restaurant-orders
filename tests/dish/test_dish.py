from src.models.dish import Dish  # noqa: F401, E261, E501
from models.ingredient import Ingredient, Restriction
import pytest


# Req 2
def test_dish():
    ingredient = Ingredient("Frango")
    dish_frango = Dish("Frango Teriaki", 25.0)
    assert dish_frango.name == "Frango Teriaki"
    assert dish_frango.recipe == {}

    dish_frango.add_ingredient_dependency(ingredient, 5)
    assert dish_frango.recipe == {ingredient: 5}
    assert dish_frango.get_ingredients() == {ingredient}

    assert dish_frango.__eq__(dish_frango) == True

    assert dish_frango.__hash__() == hash("Dish('Frango Teriaki', R$25.00)")

    assert dish_frango.get_restrictions() == ingredient.restrictions

    with pytest.raises(TypeError):
        Dish("Frango Teriaki", "25.0")

    with pytest.raises(ValueError):
        Dish("Frango Teriaki", -25.0)
