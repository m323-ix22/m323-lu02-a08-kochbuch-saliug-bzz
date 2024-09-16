"""
Dieses Modul bearbeitet JSON-basierte Rezepte und passt die Mengenangaben
an eine variable Anzahl von Personen an. Es verwendet Pure Functions und Immutable Data.
"""

import json


def adjust_recipe(original_recipe, num_servings):
    """
    Passt die Mengenangaben eines Rezepts an die gegebene Anzahl an Personen an.

    Args:
        original_recipe (dict): Das ursprüngliche Rezept als Dictionary.
        num_servings (int): Die Anzahl der Personen, für die das Rezept angepasst werden soll.

    Returns:
        dict: Ein neues, angepasstes Rezept mit den Mengenangaben für die gegebene Anzahl von Personen.
    """
    factor = num_servings / original_recipe["servings"]
    adjusted_ingredients = {ingredient: int(amount * factor) for ingredient,
                                                                 amount in original_recipe["ingredients"].items()}

    # Rückgabe eines neuen Rezept-Dictionarys
    return {
        "title": original_recipe["title"],
        "ingredients": adjusted_ingredients,
        "servings": num_servings
    }


def load_recipe(json_string):
    """
    Wandelt einen JSON-kodierten String in ein Python-Dictionary um.

    Args:
        json_string (str): Der Rezept-String im JSON-Format.

    Returns:
        dict: Das Rezept als Python-Dictionary.
    """
    return json.loads(json_string)


if __name__ == "__main__":
    # Beispiel für die Datenstruktur eines Rezepts
    json_recipe = '{"title": "Spaghetti Bolognese", "ingredients": {"Spaghetti": 400, "Tomato Sauce": 300, ' \
                  '"Minced Meat": 500}, "servings": 4}'

    # Rezept laden
    recipe_data = load_recipe(json_recipe)

    # Rezept anpassen
    servings = 2
    adjusted_recipe_data = adjust_recipe(recipe_data, servings)

    # Ergebnisse anzeigen
    print("Originalrezept:", recipe_data)
    print("Angepasstes Rezept:", adjusted_recipe_data)
