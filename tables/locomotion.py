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
                      "Tropical Lagoon": {2: "Immobile", 3: "Immobile",
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
                      # FIXME: How would we get to this?
                      "Planetary Interior": {2: "Immobile", 3: "Immobile",
                                             4: "Immobile", 5: "Immobile",
                                             6: "Immobile", 7: "Digging",
                                             8: "Digging", 9: "Digging",
                                             10: "Digging", 11: "Digging",
                                             12: "Digging", 13: "Digging"
                                             },
                      "River/Stream": {2: "Immobile", 3: "Immobile",
                                       4: "Floating", 5: "Slithering*",
                                       6: "Digging (water)*", 7: "Walking*",
                                       8: "Swimming", 9: "Swimming",
                                       10: "Winged Flight*", 11: "Winged Flight*",
                                       12: "Special", 13: "Special"
                                       },
                      "Salt-Water Sea": {2: "Immobile", 3: "Immobile",
                                         4: "Floating", 5: "Walking*",
                                         6: "Slithering*", 7: "Swimming",
                                         8: "Swimming", 9: "Swimming",
                                         10: "Winged Flight*", 11: "Winged Flight*",
                                         12: "Special", 13: "Special"
                                         },
                      # FIXME: How would we get to this, and what do these specials affect?
                      "Space-Dwelling": {2: "Immobile", 3: "Immobile",
                                         4: "Immobile", 5: "Immobile",
                                         6: "Immobile", 7: "Solar Sail",
                                         8: "Solar Sail", 9: "Solar Sail",
                                         10: "Solar Sail", 11: "Solar Sail",
                                         12: "Rocket", 13: "Rocket"
                                         },
                      "Swampland": {2: "Immobile", 3: "Swimming*",
                                    4: "Swimming*", 5: "Swimming*",
                                    6: "Slithering", 7: "Digging (land)*",
                                    8: "Walking", 9: "Climbing*",
                                    10: "Winged Flight*", 11: "Winged Flight*",
                                    12: "Special", 13: "Special"
                                    },
                      "Woodlands": {2: "Immobile", 3: "Slithering",
                                    4: "Slithering", 5: "Digging (land)*",
                                    6: "Walking", 7: "Walking",
                                    8: "Climbing*", 9: "Climbing*",
                                    10: "Winged Flight*", 11: "Winged Flight*",
                                    12: "Special", 13: "Special"
                                    },
                      "Jungle": {2: "Immobile", 3: "Slithering",
                                 4: "Slithering", 5: "Digging (land)*",
                                 6: "Walking", 7: "Walking",
                                 8: "Climbing*", 9: "Climbing*",
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
