import unittest

import species
import tables
import random


class TestSpecies(unittest.TestCase):

    def setUp(self):
        random.seed(1)  # Ensure that our tests are reproducible
        self.species = species.Species()

    def testInit(self):
        self.assertIn(self.species.chemical_base, tables.ChemicalBases)

        # We rolled a land dwelling species
        self.assertTrue(self.species.land_dwelling)

        # Hence, the habitat is one of the land-based ones
        self.assertIn(self.species.habitat, tables.LandHabitats)
        self.assertNotIn(self.species.habitat, tables.WaterHabitats)

        # Possible sapients
        self.assertTrue(self.species.sapient)

        # We didn't roll a combined method, so only one strategy
        self.assertTrue(len(self.species.trophic_level) == 1)
        self.assertIn(self.species.trophic_level, tables.TrophicStrategy)

    def testCompatibleHabitatTrophicLevel(self):
        self.assertTrue(self.species.habitat == "Deep-Ocean Vent")
        self.assertFalse(self.species.trophic_level == "Photosynthetic")
