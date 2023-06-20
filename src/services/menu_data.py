# Req 3
import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = self.get_dishes(source_path)

    def get_dishes(self, path):
        dishes = {}
        with open(path, "r") as file:
            reader = csv.reader(file)
            next(reader)

            for line in reader:
                dish_name, price, ingredient_name, recipe_amount = line

                if dish_name not in dishes:
                    dishes[dish_name] = Dish(dish_name, float(price))

                ingredient = Ingredient(ingredient_name)
                dishes[dish_name].add_ingredient_dependency(
                    ingredient, int(recipe_amount)
                )

        return set(dishes.values())
