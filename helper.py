recipes = {"Sourdough Bread": {'type': 'Savory',
                         'description': "Regular Sourdough Bread",
                         'ingredients': {"All-purpose flour": "500 g", "Sourdough starter": "100 g",
                                         "Filtered water": '350 g', "Salt": '10 g', },
                         'instructions': {
                             "Mix flour with water until there are no lumps": "3 min",
                             "Wait for the flour to fully absorb the water (autolysis)": "30 min",
                             "Add the sourdough stater and salt": " 3 min",
                             "Give it some rest": "20 min",
                             "Mix it well, by hand or with a stand-mixer": "10 min",
                             "1st bulk fermentation step": "60 min",
                             "1st stretch and fold": "2 min",
                             "2nd bulk fermentation step": "60 min",
                             "2nd stretch and fold on all four sides of the dough": "2 min",
                             "3rd bulk fermentation step": "60 min",
                             "3rd stretch and fold on all four sides of the dough": "2 min",
                             "4th bulk fermentation step": "60 min",
                             "Dust the top counter with flour and pour the dough gently": "1 min",
                             "Stretch and fold on all four sides of the dough, turn it upside down": "1 min",
                             "Tighten the dough by pushing it on all sides, trying to create a ball-like shape. \
                             Don't tighten it too much, the gluten network doesn't break": "2 min",
                             "Give it some rest": "20 min",
                             "Stretch the dough, making it into a rectangular shape. Fold the two largest sides on top of each other."
                             "Turn the dough in 90 degrees and roll it, always adding tension, until there is no more dough to roll. ": "3 min",
                             "Transfer your dough to your duste banetton": "1 min",
                             "Let it proof": " 30 min",
                             "Cover it with a plastic bag and let it rest over night in the fridge": "12 h"
                         },
                         'comments': ["Mouth watering"]
                         }
           }

def add_ingredients(recipe_name=None, text=None):
    if recipe_name and text:
        text_list = text.split(",")
        recipes[recipe_name]['ingredients'] = dict.fromkeys(text_list)


def add_instructions(recipe_name=None, text=None):
    if recipe_name and text:
        text_list = text.split(",")
        recipes[recipe_name]['instructions'] = dict.fromkeys(text_list)

        # instructions_dict = {}
        # for i, instruction in enumerate(text_list):
        #     instructions_dict["Step {}".format(i + 1)] = instruction
        # recipes[recipe_name]['instructions'] = instructions_dict
