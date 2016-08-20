import random
from collections import defaultdict
import typing

from dice import DiceRoller
import lookups


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
        else:
            self.planet = defaultdict

        self.chemical_base = self.make_chemical_base()
        self.sphere = self.make_sphere()
        self.habitat = self.make_habitat()
        self.trophic_level = self.make_trophic_level()
        self.locomotion, self.secondary_locomotion, self.tertiary_locomotion = self.make_locomotion()
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
            return lookups.ChemicalBases[0]
        if dice_roll <= 7:
            return lookups.ChemicalBases[1]
        if dice_roll == 8:
            return lookups.ChemicalBases[2]
        if dice_roll <= 11:
            return lookups.ChemicalBases[3]
        if dice_roll == 12:
            return lookups.ChemicalBases[4]
        if dice_roll == 13:
            return lookups.ChemicalBases[5]
        if dice_roll == 14:
            return lookups.ChemicalBases[6]
        if dice_roll == 15:
            return lookups.ChemicalBases[7]
        if dice_roll == 16:
            return lookups.ChemicalBases[8]
        if dice_roll <= 18:
            return lookups.ChemicalBases[9]

    def make_sphere(self):
        """

        :return:
        """
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

    def make_habitat(self) -> str:
        """
        Based on the type of planet, choose a habitat for the species.
        :return: The habitat.
        """
        if self.constraints["Habitat"] is not None:
            return self.constraints["Habitat"]

        # Gas Giants use the water table
        # FIXME: Locomotion treats Gas Giant as a habitat though!
        if self.planet["Type"] == "Gas Giant":
            habitat_table = lookups.WaterHabitats
        else:
            # This should be the normal case!
            habitat_table = lookups.LandHabitats if self.sphere == "Land" else lookups.WaterHabitats

        # There is only option in this special case
        if self.planet["Hydrographic Cover"] == 100 and self.sphere == "Land":
            return "Island/Beach"

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

    def make_trophic_level(self):
        """
        Determine the way that this species fuels its energy needs.
        :return: A list of one or two ways that the species gets its energy.
        """
        if self.constraints["Trophic Level"] is not None:
            return self.constraints["Trophic Level"]

        if self.constraints["Sapient"] is not None:
            sapient = self.constraints["Sapient"]
        else:
            sapient = False

        trophic_levels = []
        dice_roll = [DiceRoller.roll_dice(3, 0)]
        # If we rolled a three, roll twice and ensure no further threes.
        if dice_roll[0] == 3:
            dice_roll = [DiceRoller.roll_dice(3, 0), DiceRoller.roll_dice(3, 0)]
        for roll in dice_roll:
            while roll == 3:
                roll = DiceRoller.roll_dice(3, 0)

        for roll in dice_roll:
            trophic_levels.append(lookups.get_trophic_level(roll, sapient, self.habitat))

        return trophic_levels

    def make_locomotion(self) -> tuple([str, str, str]):
        """

        :return: A list of methods of locomotion.
        """
        if self.trophic_level in ["Pouncing Carnivore", "Chasing Carnivore",
                                  "Omnivore", "Gathering Herbivore", "Scavenger"]:
            roll_mod = 1
        else:
            roll_mod = 0

        dice_roll = DiceRoller.roll_dice(2, roll_mod)

        primary_locomotion = lookups.get_locomotion(self.habitat, dice_roll, True)
        secondary_locomotion = ""
        tertiary_locomotion = ""
        if primary_locomotion.endswith("*"):
            dice_roll = DiceRoller.roll_dice(2, 0)
            primary_locomotion = primary_locomotion[:-1]
            secondary_locomotion = lookups.get_locomotion(primary_locomotion, dice_roll)

        if secondary_locomotion.endswith("*"):
            dice_roll = DiceRoller.roll_dice(2, 0)
            secondary_locomotion = secondary_locomotion[:-1]
            tertiary_locomotion = lookups.get_locomotion(primary_locomotion, dice_roll)
            # Tertiary comes from the same table as secondary, ensure that it isn't the same and doesn't end in "*"
            if tertiary_locomotion.endswith("*"):
                tertiary_locomotion = tertiary_locomotion[:-1]
            if tertiary_locomotion == secondary_locomotion:
                tertiary_locomotion = ""

        return primary_locomotion, secondary_locomotion, tertiary_locomotion



