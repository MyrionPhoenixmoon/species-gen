import random
from collections import defaultdict

from dice import DiceRoller
import tables


class Species:

    def __init__(self, seed=None, config=None):
        """
        Generate a species according to the framework in GURPS Space.

        :param seed: A seed for the RNG, to generate reproducible objects.
        :param config: Predetermined information that should be taken into account during species generation.
        """
        if seed is not None:
            seed = int(seed)
        random.seed(seed)

        self.constraints = defaultdict()
        # Have some parameters been fixed?
        if config.species is not None:
            self.constraints.update(config.species)

        if config.planet is not None:
            self.planet = config.planet

        self.details = {}
        self.chemical_base = self.make_chemical_base()
        self.sphere = self.make_sphere()
        self.habitat = self.make_habitat()
        self.trophic_level = self.make_trophic_level()
        self.size = self.make_size()
        self.symmetry = self.make_symmetry()
        self.no_of_limbs = self.make_limbs()
        self.tail = self.make_tails()
        self.manipulators = self.make_manipulators()
        self.skeleton = self.make_skeleton()
        self.skin = self.make_skin()
        self.breathing = self.make_breathing()
        self.temperature = self.make_temperature()
        self.growth = self.make_growth()
        self.sexes = self.make_sexes()
        self.gestation = self.make_gestation()
        self.strategy = self.make_strategy()
        self.senses = self.make_senses()
        self.intelligence = self.make_intelligence()
        self.mental_qualities = self.make_mental_qualities()

    def make_chemical_base(self) -> str:
        """
        Determine the chemical basis for this lifeform.
        :return: A string with the chemical base of the species.
        """
        if self.constraints["Chemical Base"] is not None:
            return self.constraints["Chemical Base"]

        dice_roll = DiceRoller.roll_dice(3, 0)

        if dice_roll <= 5:
            return tables.ChemicalBases[0]
        if dice_roll <= 7:
            return tables.ChemicalBases[1]
        if dice_roll == 8:
            return tables.ChemicalBases[2]
        if dice_roll <= 11:
            return tables.ChemicalBases[3]
        if dice_roll == 12:
            return tables.ChemicalBases[4]
        if dice_roll == 13:
            return tables.ChemicalBases[5]
        if dice_roll == 14:
            return tables.ChemicalBases[6]
        if dice_roll == 15:
            return tables.ChemicalBases[7]
        if dice_roll == 16:
            return tables.ChemicalBases[8]
        if dice_roll <= 18:
            return tables.ChemicalBases[9]

    def make_sphere(self):
        if self.constraints["Sphere"] is not None:
            return self.constraints["Sphere"]

        roll_mod = 0
        # Modify by +/-2 for high or low hydrographic cover
        if self.planet["Hydrographic Cover"] <= 50:
            roll_mod -= 1
        if self.planet["Hydrographic Cover"] <= 10:
            roll_mod -= 1

        if self.planet["Hydrographic Cover"] >= 80:
            roll_mod += 1
        if self.planet["Hydrographic Cover"] >= 90:
            roll_mod += 1

        if DiceRoller.roll_dice(1, roll_mod) <= 3:
            return "Land"
        else:
            return "Water"

    def make_habitat(self):
        if self.constraints["Habitat"] is not None:
            return self.constraints["Habitat"]

        # There is only option in this special case
        if self.planet["Hydrographic Cover"] == 100 and self.sphere == "Land":
            return "Island/Beach"

        # Gas Giants use the water table
        if self.planet["Type"] == "Gas Giant":
            habitat_table = tables.WaterHabitats
        else:
            # This should be the normal case!
            habitat_table = tables.LandHabitats if self.sphere == "Land" else tables.WaterHabitats

        # There are only a few allowed options in this special case
        if self.planet["Hydrographic Cover"] == 0 and self.sphere == "Water":
            allowed_habitats = ["Salt-Water Sea", "Fresh-Water Lake", "River/Stream"]
        else:
            # Again, normal case, anything goes
            allowed_habitats = habitat_table

        habitat = ""
        while habitat not in allowed_habitats:
            dice_roll = DiceRoller.roll_dice(3, 0)
            if dice_roll <= 7:
                habitat = habitat_table[0]
            if dice_roll == 8:
                habitat = habitat_table[1]
            if dice_roll == 9:
                habitat = habitat_table[2]
            if dice_roll == 10:
                habitat = habitat_table[3]
            if dice_roll == 11:
                habitat = habitat_table[4]
            if dice_roll == 12:
                habitat = habitat_table[5]
            if dice_roll == 13:
                habitat = habitat_table[6]
            if dice_roll >= 14:
                habitat = habitat_table[7]

        return habitat


