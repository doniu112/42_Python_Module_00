def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    g_word: str
    if unit == "packets":
        g_word = f"{quantity} {unit} available"
    elif unit == "grams":
        g_word = f"{quantity} {unit} total"
    elif unit == "area":
        g_word = f"covers {quantity} square meters"
    else:
        print("Unknown unit type")
        return
    print(f"{seed_type.capitalize()} seeds: {g_word}")
