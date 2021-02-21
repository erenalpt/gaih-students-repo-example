class Cook:
    def __init__(self, time, cal, material):
        self.time = time
        self.cal = cal
        self.material = material

    def CookTime(self):
        print("After {} minutes, your meal is ready.".format(self.time))

    def CookOrder(self):
        for i in range(len(self.material)):
            print("{} add to the meal.".format(self.material[i]))

    def CalPrint(self):
        print("You got {} calories from this meal. Bon Appetit.\n".format(self.cal))


class Meal(Cook):
    def __init__(self, name, time, cal, material):
        super().__init__(time, cal, material)
        self.name = name

    def Ready(self):
        print("If you're ready, let's start preparing the {}".format(self.name))


steak = Meal("Steak", 30, 108, ["Steak", "Salt", "Black Pepper", "Cumin"])
steak.Ready()
steak.CookOrder()
steak.CookTime()
steak.CalPrint()

beef = Meal("Beef", 20, 231, ["Beef", "Olive oil", "500 grams of wild mushroom mix", "1 branch of thyme", "2 egg yolks",
                              "Salt"])
beef.Ready()
beef.CookOrder()
beef.CookTime()
beef.CalPrint()

stew = Meal("Chickpea stew", 50, 90, ["2 cups chickpeas", "500 grams of beef", "500 grams of wild mushroom mix",
                                      "Olive oil", "250 grams of shallots", "Pepper paste", "Salt"])
stew.Ready()
stew.CookOrder()
stew.CookTime()
stew.CalPrint()

"""
OUTPUT:

If you're ready, let's start preparing the Steak
Steak add to the meal.
Salt add to the meal.
Black Pepper add to the meal.
Cumin add to the meal.
After 30 minutes, your meal is ready.
You got 108 calories from this meal. Bon Appetit.

If you're ready, let's start preparing the Beef
Beef add to the meal.
Olive oil add to the meal.
500 grams of wild mushroom mix add to the meal.
1 branch of thyme add to the meal.
2 egg yolks add to the meal.
Salt add to the meal.
After 20 minutes, your meal is ready.
You got 231 calories from this meal. Bon Appetit.

If you're ready, let's start preparing the Chickpea stew
2 cups chickpeas add to the meal.
500 grams of beef add to the meal.
500 grams of wild mushroom mix add to the meal.
Olive oil add to the meal.
250 grams of shallots add to the meal.
Pepper paste add to the meal.
Salt add to the meal.
After 50 minutes, your meal is ready.
You got 90 calories from this meal. Bon Appetit.
"""
