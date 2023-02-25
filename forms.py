from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, RadioField, IntegerField, FieldList, FormField, Form
from wtforms.validators import DataRequired


class RecipeForm(FlaskForm):
    recipe = StringField("Recipe", validators=[DataRequired()])
    recipe_categories = [("Sourdough", "Sourdough"), ("Baker's Yeast", "Baker's Yeast")]
    ingredients = TextAreaField("Ingredients", validators=[DataRequired()])
    recipe_type = RadioField("Type", choices=recipe_categories)
    description = StringField("Description", validators=[DataRequired()])
    instructions = TextAreaField("Instructions", validators=[DataRequired()])
    submit = SubmitField("Add Recipe")

class CommentForm(FlaskForm):
    comment = StringField("Comment", validators=[DataRequired()])
    submit = SubmitField("Add Comment")


class InstructionForm(FlaskForm):
    instruction = StringField("Instructions", validators=[DataRequired()])
    step_duration = IntegerField("Duration (min)", validators=[DataRequired()])

class IngredientForm(Form):
    ingredient = StringField("Ingredient", validators=[DataRequired()])
    ingredient_quantity = StringField("Ingredient Quantity", validators=[DataRequired()])

class IngredientsFormSet(FlaskForm):
    ingredient_set = FieldList(FormField(IngredientForm))
    instruction_set = FieldList(FormField(InstructionForm))
    submit = SubmitField("Add Quantities")
