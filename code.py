import random

class Pound:

    def __init__(self, rare=False): # constructor
        
        self.rare = rare
        
        if self.rare:
            self.value = 1.25
        else:
            self.value = 1
                
        self.colour = 'gold'
        self.num_edges = 1
        self.diameter = 22.5 # mm
        self.thickness = 3.15 # mm
        self.heads = True

    def rust(self):
        self.colour = 'greenish'

    def clean(self):
        self.colour = 'gold'

    def flip(self):
        heads_options = [True, False]
        choice = random.choice(heads_options)
        self.heads = choice

    def __del__(self): # destructor
        print('Coin spent')


coin1 = Pound()

print(coin1.colour)

del coin1

print(coin1.colour) 