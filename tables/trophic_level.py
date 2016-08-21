from dice import DiceRoller


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