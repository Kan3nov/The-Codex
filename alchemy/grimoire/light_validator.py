from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    ingreds = [ingred.strip() for ingred in ingredients.split(",")]
    for ingred in ingreds:
        if ingred.lower() in light_spell_allowed_ingredients():
            return ", ".join(ingreds[:-1]) + " and " + ingreds[-1] + " - VALID"
    return ", ".join(ingreds[:-1]) + " and " + ingreds[-1] + " - INVALID"
