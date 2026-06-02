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

def test_add_recipe():
    s = ShoppingList()
    recipe = Recipe("Блины")
    recipe.add_ingredient(Ingredient("Мука", 500, "г"))
    s.add_recipe(recipe, 2)
    assert len(s._items) ==1
    with pytest.raises(ValueError):
        s.add_recipe(recipe, 0)

def test_remove_recipe():
    s = ShoppingList()
    recipe =Recipe("Блины")
    recipe.add_ingredient(Ingredient("Мука",500, "г"))
    s.add_recipe(recipe, 1)
    s.remove_recipe("Блины")
    assert len(s._items) ==0

def test_get_list():
    s = ShoppingList()
    r1 = Recipe("Блины")
    r1.add_ingredient(Ingredient("Мука", 500, "г"))
    r2 = Recipe("Оладушки")
    r2.add_ingredient(Ingredient("Мука", 300, "г"))
    r2.add_ingredient(Ingredient("Молоко", 200, "мл"))
    s.add_recipe(r1,1)
    s.add_recipe(r2,1)
    items = s.get_list()
    assert len(items) == 2
    assert items[0].name =="Мука"
    assert items[0].quantity ==800.0
    assert items[1].name == "Молоко"

def test_add():
    s1 = ShoppingList()
    s2 = ShoppingList()
    r1 = Recipe("Блины")
    r1.add_ingredient(Ingredient("Мука", 300, "г"))
    s1.add_recipe(r1,1)
    s2.add_recipe(r1,2)
    s3 = s1 +s2
    assert len(s3._items)== 2