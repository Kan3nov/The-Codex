if __name__ == "__main__":
    pass
else:
    from .elements import create_air
    from .potions import strength_potion, healing_potion as heal
    from .transmutation import lead_to_gold
    create_air()
    strength_potion()
    heal()
    lead_to_gold()
