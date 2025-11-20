menu = {
    "pizza": 150,
    "burger": 55,
    "salad": 100,
    "pasta": 120
}

choice = input("What would you like to order? (pizza, burger, salad, pasta): ").lower()

if choice in menu:
    price = menu[choice]
    print(f"Great choice! The {choice} costs P{price}. Proceeding to order.")
else:
    print("Sorry, that's not on the menu. Please choose again.")
