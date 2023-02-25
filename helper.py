import numpy as np

recipes = {"fried egg": {'type': 'Breakfast',
                         'description': "Egg fried in butter",
                         'ingredients': {"Butter": '10g', "Egg": '2 units', "Salt": '2g'},
                         'instructions': {
                             "Melt butter in pan over medium-low heat": "-",
                             "Crack the egg into the buttered pan": "-",
                             "Sprinkle the pinch of salt onto cooking egg": "-",
                             "Flip egg after about a minute and a half": "-",
                         },
                         'comments': ["Yummy!!", "Egg-cellent ;->"]
                         },
           "buttered toast": {'type': 'Breakfast',
                              'description': "Toasted bread spread with butter",
                              'ingredients': {'Butter': '10g', 'Bread': '2 slices'},
                              'instructions': {
                                  "Put the bread in the toaster": 1,
                                  "Take the toast out of the toaster": "-",
                                  "Put the pad of butter on the toasted bread": "-",
                                  "Wait for the butter to meat": 1,
                                  "Spread the melted butter onto the bread": "-"
                              },
                              'comments': ["Toasty", "What a great recipe!"]
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
