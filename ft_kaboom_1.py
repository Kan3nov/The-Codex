print("=== Kaboom 1 ===")
print("Access to alchemy/grimoire/dark_spellbook.py directly")
print("Test import now - THIS WILL RAISE AN EXCEPTION")
try:
    import alchemy.grimoire.dark_spellbook
    alchemy.grimoire.dark_spellbook.dark_spell_allowed_ingredients
except Exception as e:
    print("Error: ", e)
