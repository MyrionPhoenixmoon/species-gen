# TODO: Turn these into dicts with the values to roll against or something even better?
ChemicalBases = ["Hydrogen", "Ammonia",
                 "Hydrocarbon", "Water",
                 "Chlorine", "Silicone/Sulfuric Acid",
                 "Silicone/Liquid Sulfur", "Silicon/Liquid Rock",
                 "Plasma", "Exotica"]

LandHabitats = ["Plains", "Desert",
                "Island/Beach", "Woodlands",
                "Swampland", "Mountain",
                "Arctic", "Jungle"]

WaterHabitats = ["Banks", "Open Ocean",
                 "Fresh-Water Lakes", "River/Stream",
                 "Tropical Lagoon", "Deep-Ocean Vents",
                 "Salt-Water Sea", "Reef"]

TrophicStrategy = ["Photosynthetic", "Chemosynthetic",
                   "Autotroph/Other", "Decomposer",
                   "Scavenger", "Omnivore",
                   "Gathering Herbivore", "Grazing/Browsing Herbivore",
                   "Pouncing Carnivore", "Chasing Carnivore",
                   "Trapping Carnivore", "Hijacking Carnivore",
                   "Filter-Feeder", "Parasite/Symbiont"]

# TODO: Figure out how to deal with * entries and "Special" entries
Locomotion = {"Arctic": {2: "Immobile", (3, 4): "Slithering",
                         (5, 6): "Swimming*", 7: "Digging",
                         (8, 9): "Walking", (10, 11): "Winged Flight*",
                         (12, 13): "Special"}}

