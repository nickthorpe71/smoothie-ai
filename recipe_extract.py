import json

# ML Tutorial --- https://www.kdnuggets.com/2020/07/generating-cooking-recipes-using-tensorflow.html

with open('recipes_raw/recipes_raw_nosource_fn.json', 'r') as f:
    data = json.load(f)

filtered_arr = []

for recipe in data.values():

    if recipe.get("title") is not None:
        if 'smoothie' in recipe.get("title").lower():
            cleaned_ingredients = []

            for ingredient in recipe.get("ingredients"):
                entry = ingredient.replace("ADVERTISEMENT", "").strip()
                if entry is not "":
                    cleaned_ingredients.append(entry)

            new_recipe = {
                "title": recipe.get("title"),
                "ingredients": cleaned_ingredients,
                "instructions": recipe.get("instructions")
            }

            filtered_arr.append(new_recipe)

with open('smoothie_data_cleaned_3.json', 'w') as f:
    json.dump(filtered_arr, f, indent=2)

