import random

class Coin:
    def __init__(self, rare=False, clean=True, heads=True):
        self.is_rare = rare
        self.is_clean = clean
        self.heads = choice
        
        if self.is_rare:
            self.value = self.original_value * 1.25
        else:
            self.value = self.original_value

        if self.is_clean:
            self.colour = self.clean_colour
        else:
            self.colour = self.rusty_colour

    def rust(self):
        self.colour = self.rusty_colour

    def clean(self):
        self.colour = self.clean_colour

    def __del__(self): # destructor
        print('Coin spent')

    def flip(self):
        heads_options = [True, False]
        choice = random.choice(heads_options)
        self.heads = choice

class Pound:

    