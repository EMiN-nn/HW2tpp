class Ingredient:
    def __init__(self, name, quantity,unit):
        self.name = name
        self.quantity = quantity
        self.unit = unit
    @property
    def quantity(self): return self._quantity
    @quantity.setter
    def quantity(self, value):
        value = float(value)
        if value <=0:
            raise ValueError("Количество должно быть положительным")
        self._quantity = value
    def __str__(self): return f"{self.name}: {self.quantity} {self.unit}"
    def __repr__(self): return f"Ingredient({self.name!r}, {self.quantity}, {self.unit!r})"
    def __eq__(self, value):
        if not isinstance(value,Ingredient): return False
        return self.name == value.name and self.unit == value.unit


class Recipe:
    def __init__(self, title, ingredients = None):
        self.title = title
        if ingredients is None: self.ingredients = []
        else: self.ingredients = ingredients
    def add_ingredient(self, ingredient):
        for i in self.ingredients:
            if i == ingredient:
                i.quantity += ingredient.quantity
                return
        self.ingredients.append(ingredient)
    def scale(self, ratio):
        if type(ratio) not in (float, int) or ratio <= 0:
            raise ValueError("коэффицент должен быть положительным")
        new_ingredients = []
        for i in self.ingredients:
            new_ingredient = Ingredient(i.name,i.quantity * ratio,i.unit)
            new_ingredients.append(new_ingredient)
        return Recipe(self.title, new_ingredients)
    def __len__(self): return (len(self.ingredients))
    def __str__(self):
        s = self.title
        for i in self.ingredients: s += "\n" + str(i)
        return s

class ShoppingList:
    def __init__(self):
        self._items = []

    def add_recipe(self, recipe, portions):
        if portions <= 0: raise ValueError("Количество порций должно быть положительным")
        scaled_recipe = recipe.scale(portions)
        for ingredient in scaled_recipe.ingredients: self._items.append((ingredient, recipe.title))

    def remove_recipe(self, title):
        new_items = []
        for ingredient, recipe_title in self._items:
            if recipe_title != title: new_items.append((ingredient, recipe_title))
        self._items = new_items

    def get_list(self):
        s = {}
        for ingredient, recipe_title in self._items:
            key = (ingredient.name, ingredient.unit)
            if key in s:
                s[key] += ingredient.quantity
            else:
                s[key] = ingredient.quantity
        shopping_list = []
        for key in s:
            name = key[0]
            unit = key[1]
            quantity = s[key]
            shopping_list.append(Ingredient(name, quantity, unit))
        shopping_list.sort(key=lambda ingredient: ingredient.name)
        return shopping_list

    def __add__(self, other):
        new_list = ShoppingList()
        for ingredient, recipe_title in self._items:
            new_list._items.append((ingredient, recipe_title))
        for ingredient, recipe_title in other._items:
            new_list._items.append((ingredient, recipe_title))
        return new_list
class DietaryRecipe(Recipe):
    def __init__(self, title, diet_type, ingredients=None):
        super().__init__(title, ingredients)
        self.diet_type = diet_type
    def scale(self, ratio):
        if type(ratio) not in (int, float) or ratio <= 0:
            raise ValueError("коэффициент должен быть положительным")
        new_ingredients = []
        for ingredient in self.ingredients:
            new_ingredient = Ingredient(ingredient.name,ingredient.quantity*ratio,ingredient.unit)
            new_ingredients.append(new_ingredient)
        return DietaryRecipe(self.title, self.diet_type, new_ingredients)
    def __str__(self):
        return f"[{self.diet_type}] " +super().__str__()