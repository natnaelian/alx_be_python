def display_menu():
    """Display the main menu options"""
    print("\n" + "="*30)
    print("SHOPPING LIST MANAGER".center(30))
    print("="*30)
    print("1. Add item to list")
    print("2. Remove item from list")
    print("3. View current list")
    print("4. Exit program")
    print("="*30)

def add_item(shopping_list):
    """Add an item to the shopping list"""
    item = input("\nEnter the item to add: ").strip()
    if item:
        if item.lower() in shopping_list:
            print(f"⚠️ '{item.title()}' is already in your shopping list.")
        else:
            shopping_list.append(item.lower())  # Store in lowercase for case-insensitive comparison
            print(f"✅ '{item.title()}' added to your shopping list.")
    else:
        print("⚠️ No item entered. Please try again.")

def remove_item(shopping_list):
    """Remove an item from the shopping list"""
    if not shopping_list:
        print("\nℹ️ Your shopping list is empty!")
        return
    
    print("\nCurrent list:")
    display_list(shopping_list)
    
    item = input("\nEnter the item to remove: ").strip().lower()
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"✅ '{item.title()}' removed from your shopping list.")
    else:
        print(f"⚠️ '{item.title()}' not found in your shopping list.")

def display_list(shopping_list):
    """Display the current shopping list"""
    if not shopping_list:
        print("\nℹ️ Your shopping list is empty!")
    else:
        print("\n" + "-"*30)
        print("YOUR SHOPPING LIST:".center(30))
        print("-"*30)
        for index, item in enumerate(shopping_list, start=1):
            print(f"{index}. {item.title()}")
        print("-"*30)

def main():
    """Main program function"""
    shopping_list = []
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '1':
            add_item(shopping_list)
        elif choice == '2':
            remove_item(shopping_list)
        elif choice == '3':
            display_list(shopping_list)
        elif choice == '4':
            print("\n" + "="*30)
            print("Thank you for using Shopping List Manager!")
            print("="*30 + "\n")
            break
        else:
            print("\n⚠️ Invalid choice. Please enter a number between 1 and 4.")
        
        input("\nPress Enter to continue...")  # Pause before showing menu again

if __name__ == "__main__":
    main()