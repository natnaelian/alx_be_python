def display_menu():
    """Display the main menu options"""
    print("\n" + "="*25)
    print("Shopping List Manager")
    print("="*25)
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
    print("="*25)

def add_item(shopping_list):
    """Add an item to the shopping list"""
    item = input("\nEnter the item to add: ").strip()
    if item:  # Only add if input isn't empty
        shopping_list.append(item)
        print(f"'{item}' has been added to your list.")
    else:
        print("No item entered. Please try again.")

def remove_item(shopping_list):
    """Remove an item from the shopping list"""
    if not shopping_list:
        print("\nYour shopping list is empty!")
        return
    
    print("\nCurrent list:")
    for i, item in enumerate(shopping_list, 1):
        print(f"{i}. {item}")
    
    item = input("\nEnter the item to remove: ").strip()
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' has been removed from your list.")
    else:
        print(f"'{item}' was not found in your list.")

def view_list(shopping_list):
    """Display the current shopping list"""
    if not shopping_list:
        print("\nYour shopping list is empty!")
    else:
        print("\nYour Shopping List:")
        for i, item in enumerate(shopping_list, 1):
            print(f"{i}. {item}")

def main():
    """Main program function"""
    shopping_list = []
    
    while True:
        display_menu()
        choice_input = input("\nEnter your choice (1-4): ").strip()
        try:
            choice = int(choice_input)
        except ValueError:
            print("\nInvalid choice. Please enter a number between 1 and 4.")
            input("\nPress Enter to return to menu...")
            continue
        
        if choice == 1:
            add_item(shopping_list)
        elif choice == 2:
            remove_item(shopping_list)
        elif choice == 3:
            view_list(shopping_list)
        elif choice == 4:
            print("\nGoodbye! Happy shopping!")
            break
        else:
            print("\nInvalid choice. Please enter a number between 1 and 4.")
        
        input("\nPress Enter to return to menu...")  # Pause before showing menu again

if __name__ == "__main__":
    main()