import random

class Species:

    def __init__(self, seed=None):
        if seed is not None:
            seed = int(seed)
        random.seed(seed)

        self.chemical_base = self.make_chemical_base()
        self.land_dwelling = self.land_or_water()
        self.habitat = self.make_habitat()
        self.trophic_level = self.make_trophic_level()
        self.print_info()

    def print_info(self):
        print("Code works!")
