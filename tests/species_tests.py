import unittest

import species
import tables


class TestSpecies(unittest.TestCase):

    def setUp(self):
        self.random_seed = 1  # Ensure that our tests are reproducible
        self.species = species.Species(self.random_seed)

    # This test checks basic function and plausibility
    def testRandomCreation(self):

        # TODO: When do we decide on space-dwelling or not?
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

        # We have some form of locomotion, but no secondary or even tertiary
        self.assertIn(self.species.locomotion, tables.Locomotion[self.species.habitat])
        self.assertTrue(self.species.secondary_locomotion is None)
        self.assertTrue(self.species.tertiary_locomotion is None)

        # TODO: Size and Mass, Symmetry, #of Limbs, Tails, Manipulators, Skeleton, Skin
        # TODO: Breathing, Temperature, Growth, Sexes, Gestation, (offspring) Strategy
        # TODO: Sense, Intelligence, Mental Qualities

    # This test checks whether species creation for a specific planet works correctly
    def testCreationFromPlanet(self):
        # What info do we need from a planet?
        config = {"planet": {"world_type": "Ocean", "size": "Standard", "surface_temp": "287.4",  "hydro_cover": 80}}

        new_species = species.Species(self.random_seed, config)
        # TODO: Test that new_species fits the planet

    # This test verifies that preselected elements are respected
    def testCreationWithConstraints(self):
        config = {"species": {"land_dwelling": True, "habitat": "Arctic"}}

        new_species = species.Species(self.random_seed, config)
        self.assertEqual("Arctic", new_species.habitat)
        self.assertTrue(new_species.land_dwelling)

    def testCompatibleHabitatTrophicLevel(self):
        self.assertTrue(self.species.habitat == "Deep-Ocean Vent")
        self.assertFalse(self.species.trophic_level == "Photosynthetic")
