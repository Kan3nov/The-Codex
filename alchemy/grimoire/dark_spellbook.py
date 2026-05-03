from .dark_validator import validate_ingredients

spells: list[tuple[str, str]] = []


def dark_spell_allowed_ingredients() -> list[str]:
    return ['bats', 'forgs', 'arensic', 'eyeball']


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    is_valid = validate_ingredients(ingredients)
    if is_valid[-1:-8:-1] == "INVALID":
        return "Spell rejected: (" + is_valid + ")"
    else:
        spells.append((spell_name, ingredients))
        return "Spell recorded: (" + is_valid + ")"
