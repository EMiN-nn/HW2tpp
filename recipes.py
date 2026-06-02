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