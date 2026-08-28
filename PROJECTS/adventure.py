print("=== THE FOREST ADVENTURE ===")
print("You wake up in a dark forest, There are two paths ahead.")

health = 100
inventory = []

playing = True
while playing:
    print("\nYour health:", health)
    print("Your inventory:", inventory)

    choice = input("\nDo u go LEFT or RIGHT ?").lower()
    print("Your choice:", choice)
    playing = False