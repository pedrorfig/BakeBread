import classes


def choose_bread_type(type, weight):
    assert isinstance(type, str), 'Bread type must be a string'
    assert type in ['Brioche', 'Sourdough'], 'Type of bread not available'

    if type == 'Brioche':
        bread = classes.Brioche(weight)
    elif type == 'Sourdough':
        bread = classes.SourdoughBread(weight)

    return bread


def follow_instructions(bread, weight):
    # Press the green button in the gutter to run the script.
        bun = choose_bread_type(bread, weight)
        bun.list_ingredients()
        bun.mix_ingredients()
        bun.first_rise()
        bun.deflate()
        bun.second_rise()

if __name__ == '__main__':
    follow_instructions('Brioche', 5000)
