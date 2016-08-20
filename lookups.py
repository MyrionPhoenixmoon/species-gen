from dice import DiceRoller

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


def get_trophic_level(roll: int, sapient: bool, habitat: str) -> str:
    if sapient:
        trophic_level = get_trophic_level_sapient(roll)
    else:
        trophic_level = get_trophic_level_nonsapient(roll)

    # Filter-Feeder becomes Trapping Carnivore in Arctic or Desert habitats
    if trophic_level == "Filter-Feeder" and (habitat == "Arctic" or habitat == "Desert"):
        return "Trapping Carnivore"
    # There isn't enough light near Deep-Ocean Vents for photosynthesis
    if trophic_level == "Photosynthetic" and habitat == "Deep-Ocean Vents":
        if DiceRoller.roll_dice(1, 0) > 3:
            return "Chemosynthetic"
        else:
            return "Autotroph/Other"

    return trophic_level


def get_trophic_level_nonsapient(roll: int) -> str:
    if roll == 4:
        dice_roll = DiceRoller.roll_dice(1, 0)
        if dice_roll <= 3:
            return TrophicStrategy[0]
        if dice_roll <= 5:
            return TrophicStrategy[1]
        else:
            return TrophicStrategy[2]

    else:
        if roll == 5:
            return TrophicStrategy[3]
        if roll == 6:
            return TrophicStrategy[4]
        if roll == 7:
            return TrophicStrategy[5]
        if roll == 8 or roll == 9:
            return TrophicStrategy[6]
        if roll == 10 or roll == 11:
            return TrophicStrategy[7]
        if roll == 12:
            return TrophicStrategy[8]
        if roll == 13:
            return TrophicStrategy[9]
        if roll == 14:
            return TrophicStrategy[10]
        if roll == 15:
            return TrophicStrategy[11]
        if roll == 16:
            return TrophicStrategy[12]
        if roll == 17 or roll == 18:
            return TrophicStrategy[13]


def get_trophic_level_sapient(roll: int) -> str:
    if roll == 18:
        dice_roll = DiceRoller.roll_dice(1, 0)
        if dice_roll <= 3:
            return TrophicStrategy[0]
        if dice_roll <= 5:
            return TrophicStrategy[1]
        else:
            return TrophicStrategy[2]

    else:
        if roll == 4:
            return TrophicStrategy[13]
        if roll == 5:
            return TrophicStrategy[12]
        if roll == 6:
            return TrophicStrategy[8]
        if roll == 7:
            return TrophicStrategy[4]
        if roll == 8 or roll == 9:
            return TrophicStrategy[6]
        if roll == 10:
            return TrophicStrategy[5]
        if roll == 11 or roll == 12:
            return TrophicStrategy[9]
        if roll == 13:
            return TrophicStrategy[7]
        if roll == 14:
            return TrophicStrategy[11]
        if roll == 15 or roll == 16:
            return TrophicStrategy[10]
        if roll == 17:
            return TrophicStrategy[3]


def get_locomotion(key: str, dice_roll: int, primary=False) -> str:
    """
    Look up a method of locomotion.
    :param key: Either a habitat (for primary locomotion) or the primary locomotion.
    :param dice_roll: The roll which determines the new method of locomotion.
    :param primary: Switch between looking up by habitat or primary locomotion.
    :return: A method of locomotion.
    """
    if primary:
        return Primary_Locomotion[key][dice_roll]
    else:
        return Extra_Locomotion[key][dice_roll]


# Stars indicate potential for further locomotion methods
Primary_Locomotion = {"Arctic": {2: "Immobile", 3: "Slithering",
                                 4: "Slithering", 5: "Swimming*",
                                 6: "Swimming*", 7: "Digging (land)",
                                 8: "Walking", 9: "Walking",
                                 10: "Winged Flight*", 11: "Winged Flight*",
                                 12: "Special", 13: "Special"
                                 },
                      "Banks": {2: "Immobile", 3: "Immobile",
                                4: "Floating", 5: "Sailing",
                                6: "Swimming", 7: "Swimming",
                                8: "Swimming", 9: "Winged Flight*",
                                10: "Winged Flight*", 11: "Winged Flight*",
                                12: "Special", 13: "Special"
                                },
                      "Open Ocean": {2: "Immobile", 3: "Immobile",
                                     4: "Floating", 5: "Sailing",
                                     6: "Swimming", 7: "Swimming",
                                     8: "Swimming", 9: "Winged Flight*",
                                     10: "Winged Flight*", 11: "Winged Flight*",
                                     12: "Special", 13: "Special"
                                     },
                      "Deep-Ocean Vents": {2: "Immobile", 3: "Immobile",
                                           4: "Immobile", 5: "Immobile",
                                           6: "Floating", 7: "Digging (water)*",
                                           8: "Walking*", 9: "Walking*",
                                           10: "Swimming", 11: "Swimming",
                                           12: "Swimming", 13: "Swimming"
                                           },
                      "Reef": {2: "Immobile", 3: "Immobile",
                               4: "Immobile", 5: "Immobile",
                               6: "Floating", 7: "Digging (water)*",
                               8: "Walking*", 9: "Walking*",
                               10: "Swimming", 11: "Swimming",
                               12: "Swimming", 13: "Swimming"
                               },
                      "Desert": {2: "Immobile", 3: "Slithering",
                                 4: "Slithering", 5: "Digging (land)*",
                                 6: "Walking", 7: "Walking",
                                 8: "Walking", 9: "Winged Flight*",
                                 10: "Winged Flight*", 11: "Winged Flight*",
                                 12: "Special", 13: "Special"
                                 },
                      "Gas Giant": {2: "Swimming", 3: "Swimming",
                                    4: "Swimming", 5: "Swimming",
                                    6: "Winged Flight", 7: "Winged Flight",
                                    8: "Winged Flight", 9: "Buoyant Flight",
                                    10: "Buoyant Flight", 11: "Buoyant Flight",
                                    12: "Buoyant Flight", 13: "Buoyant Flight"
                                    },
                      "Island/Beach": {2: "Immobile", 3: "Slithering",
                                       4: "Slithering", 5: "Digging (water)*",
                                       6: "Walking", 7: "Walking",
                                       8: "Climbing*", 9: "Swimming*",
                                       10: "Winged Flight", 11: "Winged Flight",
                                       12: "Special", 13: "Special"
                                       },
                      "Lagoon": {2: "Immobile", 3: "Immobile",
                                 4: "Immobile", 5: "Floating",
                                 6: "Slithering*", 7: "Walking*",
                                 8: "Digging (water)*", 9: "Swimming",
                                 10: "Winged Flight", 11: "Winged Flight",
                                 12: "Special", 13: "Special"
                                 },
                      "Fresh-Water Lakes": {2: "Immobile", 3: "Immobile",
                                            4: "Floating", 5: "Walking*",
                                            6: "Slithering*", 7: "Swimming",
                                            8: "Swimming", 9: "Swimming",
                                            10: "Winged Flight*", 11: "Winged Flight*",
                                            12: "Special", 13: "Special"
                                            },
                      "Mountain": {2: "Immobile", 3: "Slithering",
                                   4: "Slithering", 5: "Digging (land)*",
                                   6: "Walking*", 7: "Walking*",
                                   8: "Climbing*", 9: "Winged Flight*",
                                   10: "Winged Flight*", 11: "Winged Flight*",
                                   12: "Special", 13: "Special"
                                   },
                      "Plains": {2: "Immobile", 3: "Slithering",
                                 4: "Slithering", 5: "Digging (land)*",
                                 6: "Walking", 7: "Walking",
                                 8: "Walking", 9: "Winged Flight*",
                                 10: "Winged Flight*", 11: "Winged Flight*",
                                 12: "Special", 13: "Special"
                                 },
                      # FIXME: How would we get to this? (Also 2-6: Immobile, 7-13: Digging)
                      "Planetary Interior": {2: "Immobile", 7: "Digging"
                                             },
                      "Salt-Water Sea": {2: "Immobile", 3: "Immobile",
                                            4: "Floating", 5: "Walking*",
                                            6: "Slithering*", 7: "Swimming",
                                            8: "Swimming", 9: "Swimming",
                                            10: "Winged Flight*", 11: "Winged Flight*",
                                            12: "Special", 13: "Special"
                                         }
                      }

Extra_Locomotion = {"Climbing": {2: "Slithering", 3: "Slithering",
                                 4: "Slithering", 5: "Slithering",
                                 6: "Slithering", 7: "Walking",
                                 8: "Walking", 9: "Walking",
                                 10: "Walking", 11: "Walking",
                                 12: ""
                                 },
                    "Digging (land)": {2: "Slithering", 3: "Slithering",
                                       4: "Slithering", 5: "Slithering",
                                       6: "Slithering", 7: "Walking",
                                       8: "Walking", 9: "Walking",
                                       10: "Walking", 11: "Walking",
                                       12: ""
                                       },
                    "Digging (water)": {2: "Slithering*", 3: "Slithering*",
                                        4: "Slithering*", 5: "Slithering*",
                                        6: "Walking*", 7: "Walking*",
                                        8: "Swimming", 9: "Swimming",
                                        10: "Swimming", 11: "Swimming",
                                        12: ""
                                        },
                    "Slithering": {2: "Swimming", 3: "Swimming",
                                   4: "Swimming", 5: "Swimming",
                                   6: "Swimming", 7: "Swimming",
                                   8: "Swimming", 9: "Swimming",
                                   10: "Swimming", 11: "",
                                   12: ""
                                   },
                    "Swimming": {2: "Slithering", 3: "Slithering",
                                 4: "Slithering", 5: "Slithering",
                                 6: "Slithering", 7: "Walking",
                                 8: "Walking", 9: "Walking",
                                 10: "", 11: "", 12: ""},
                    "Walking": {2: "Swimming", 3: "Swimming",
                                4: "Swimming", 5: "Swimming",
                                6: "Swimming", 7: "Swimming",
                                8: "Swimming", 9: "",
                                10: "", 11: "", 12: ""
                                },
                    "Winged Flight": {2: "Climbing*", 3: "Climbing*",
                                      4: "Climbing*", 5: "Climbing*",
                                      6: "Swimming*", 7: "Swimming*",
                                      8: "Walking", 9: "Walking",
                                      10: "Walking", 11: "Slithering*",
                                      12: ""}

                    }
