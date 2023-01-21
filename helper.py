recipes = {"fried egg": {'type': 'Breakfast',
                         'description': "Egg fried in butter",
                         'ingredients': {"Butter": '10g', "Egg": '2 units', "Salt": '2g'},
                         'instructions': {"Step 2": "Crack the egg into the buttered pan",
                                          "Step 5": "Serve egg after about a minute and a half",
                                          "Step 1": "Melt butter in pan over medium-low heat",
                                          "Step 4": "Flip egg after about a minute and a half",
                                          "Step 3": "Sprinke the pinch of salt onto cooking egg"},
                         'comments': ["Yummy!!", "Egg-cellent ;->"]
                         },
           "buttered toast": {'type': 'Breakfast',
                              'description': "Toasted bread spread with butter",
                              'ingredients': {'Butter': '10g', 'Bread': '2 slices'},
                              'instructions': {"Step 3": "Put the pad of butter on the toasted bread",
                                               "Step 4": "After a minute spread the melted butter onto the bread",
                                               "Step 1": "Put the bread in the toaster",
                                               "Step 2": "Take the toast out of the toaster"},
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
        instructions_dict = {}
        for i, instruction in enumerate(text_list):
            instructions_dict["Step {}".format(i + 1)] = instruction
        recipes[recipe_name]['instructions'] = instructions_dict
