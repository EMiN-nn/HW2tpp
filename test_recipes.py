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
def test_create_recipe():
    recipe = Recipe("Блины")
    assert recipe.title == "Блины"
    assert recipe.ingredients == []
def test_add_ingredient():
    recipe = Recipe("Блины")
    recipe.add_ingredient(Ingredient("Мука", 400, "гр"))
    recipe.add_ingredient(Ingredient("Мука", 60, "гр"))
    assert len(recipe) == 1
    assert recipe.ingredients[0].quantity == 460.0
def test_scale():
    recipe = Recipe("Блины")
    recipe.add_ingredient(Ingredient("Мука", 400, "гр"))
    scaled = recipe.scale(2)
    assert scaled is not recipe
    assert scaled.ingredients[0].quantity == 800.0
    with pytest.raises(ValueError):
        recipe.scale(-1)
def test_len():
    recipe = Recipe("Блины")
    recipe.add_ingredient(Ingredient("Мука", 340, "гр"))
    recipe.add_ingredient(Ingredient("Молоко", 500, "мл"))
    assert len(recipe) == 2
