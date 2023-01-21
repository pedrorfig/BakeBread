import numpy as np
from flask import Flask, render_template, request, redirect, url_for
from helper import recipes, add_ingredients, add_instructions
from forms import RecipeForm, CommentForm, IngredientsFormSet, IngredientForm, InstructionForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecret"


@app.route("/")
def index():
    return render_template("index.html", template_recipes=recipes)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/recipe/<string:name>", methods=["GET", "POST"])
def recipe(name):
    comment_form = CommentForm(csrf_enabled=False)
    if comment_form.validate_on_submit():
        new_comment = comment_form.comment.data
        recipes[name]['comments'].append(new_comment)
    return render_template("recipe.html", template_recipe=name, template_type=recipes[name]['type'],
                           template_description=recipes[name]['description'], template_ingredients=recipes[name]['ingredients'],
                           template_instructions=recipes[name]['instructions'], template_comments=recipes[name]['comments'],
                           template_form=comment_form)

@app.route("/add_recipe", methods=["GET", "POST"])
def new_recipe():
    recipe_form = RecipeForm(csrf_enabled=False)
    if recipe_form.validate_on_submit():
        name = recipe_form.recipe.data
        recipes[name] = {}
        recipes[name]['type'] = recipe_form.recipe_type.data
        recipes[name]['description'] = recipe_form.description.data
        new_instructions = recipe_form.instructions.data
        add_instructions(name, new_instructions)
        new_ingredients = recipe_form.ingredients.data
        add_ingredients(name, new_ingredients)
        recipes[name]['comments'] = []
        return redirect(url_for("new_ingredients_quantity", name=name))

    return render_template("new_recipe.html", template_form=recipe_form)


@app.route("/add_recipe/new_ingredients/<string:name>", methods=["GET", "POST"])
def new_ingredients_quantity(name):
    ingredients_form = IngredientsFormSet()
    ingredients = recipes[name]['ingredients']
    if ingredients_form.validate_on_submit():
        ingredient_items = ingredients_form.ingredient_set.entries
        for ingredient_item in ingredient_items:
            ingredients[ingredient_item.data['ingredient']] = ingredient_item.data['ingredient_weight']
        return redirect(url_for("index"))
    for ingredient in recipes[name]['ingredients']:
        ingredient_form = IngredientForm()
        ingredient_form.ingredient = ingredient
        ingredient_form.ingredient_weight = ""
        ingredients_form.ingredient_set.append_entry(ingredient_form)
    for instruction in recipes[name]['instructions']:
        instruction_form = InstructionForm()
        instruction_form.instruction = instruction
        instruction_form.step_duration = ""
        ingredients_form.instruction_set.append_entry(instruction_form)
    return render_template("new_recipe_ingredients.html", template_ingredients_form=ingredients_form)