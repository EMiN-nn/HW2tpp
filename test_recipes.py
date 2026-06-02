import pytest
from recipes import Ingredient, Recipe,ShoppingList,DietaryRecipe

def test_create_ingredient():
    ingredient = Ingredient("Мука",500, "г")
    assert ingredient.name == "Мука"
    assert ingredient.quantity == 500.0
    assert ingredient.unit == "г"
def test_ingredient_str():
    ingredient = Ingredient("Мука", 500,"г")
    assert str(ingredient) == "Мука: 500.0 г"
def test_ingredient_eq():
    a = Ingredient("Мука", 500, "г")
    b = Ingredient("Мука", 1000, "г")
    c = Ingredient("Сода", 1000, "г")
    d = Ingredient("Мука", 500, "т")
    assert a == b
    assert a !=c
    assert a !=d
