spells: list[tuple[str, str]] = []


def light_spell_allowed_ingredients() -> list[str]:
    return ['earth', 'air', 'fire', 'water']


def light_spell_record(spell_name: str, ingredients: str) -> str:
    from .light_validator import validate_ingredients
    is_valid = validate_ingredients(ingredients)
    if is_valid[-7:] == "INVALID":
        return "Spell rejected: (" + is_valid + ")"
    else:
        spells.append((spell_name, ingredients))
        return "Spell recorded: (" + is_valid + ")"
