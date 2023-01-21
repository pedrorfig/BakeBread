import time
import actions

MILK_DENSITY = 1.035
EGG_WEIGHT = 0.06
EGG_YOLK_WEIGHT = EGG_WEIGHT*0.58
EGG_WHITE_WEIGHT = EGG_WEIGHT*0.31

class Bread:

    def __init__(self, flour_weight):
        self.flour_weight = flour_weight

    def list_ingredients(self):
        print(dir(self))
        actions.ask_to_continue()

    def mix_ingredients(self):
        print("Mix all ingredients in a bowl")
        actions.ask_to_continue()

    def first_rise(self, room_temperature=20):
        print("Let it rise until it doubles in size")
        actions.ask_to_continue()

    def deflate(self):
        print("Punch it down")
        actions.ask_to_continue()

    def second_rise(self):
        pass

    def bake(self):
        pass

    def cool(self):
        pass
class YeastBread(Bread):
    def proof_yeast(self):
        pass
    def knead(self, knead_time):

        assert knead_time is int, "Knead time must be an integer"

        print("Start kneading your dough")
        time.sleep(knead_time)
        print("We're done kneading")

class Brioche(YeastBread):
    """

    """
    def __init__(self, flour_weight):
        Bread.__init__(self, flour_weight)
        self.milk_vol = self.flour_weight*0.4
        self.sugar_weight = self.flour_weight*0.16
        self.num_eggs = self.flour_weight*0.004
        self.butter_weight = self.flour_weight*0.16
        self.salt_weight = self.flour_weight*0.01
        self.dry_yeast_weight = self.flour_weight*0.02

class SourdoughBread(Bread):
    pass