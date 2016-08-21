from dice import DiceRoller


def make_size_and_weight(size_category):
    """

    :param size_category:
    :return:
    """
    dice_roll = DiceRoller.roll_dice(1, 0)

    # Massive creatures are special and can be almost arbitrarily large
    if size_category == "Large" and dice_roll == 6:
        size = DiceRoller(2, 0) * 10
        weight = ((size/2) ** 3) * 200
        return size, weight

    return size_weight_table[size_category][dice_roll-1]

size_weight_table = {
    # Yards, Pounds
    "Small": [(0.05, 0.003), (0.07, 0.01),
              (0.1, 0.025), (0.15, 0.08),
              (0.2, 0.2), (0.3, 1)],
    "Human-Scale": [(0.5, 4), (0.7, 9),
                    (1, 25), (1.5, 80),
                    (2, 200), (3, 600)],
    "Large": [(5, 3000), (7, 4000),
              (10, 12000), (15, 40000),
              (20, 100000)]
}
