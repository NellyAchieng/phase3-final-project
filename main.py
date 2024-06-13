#!/usr/bin/env python3

from models import ShoppingListManager

def main():
    manager = ShoppingListManager()
    while True:
        manager.display_help()
        command = input("Enter your command: ").strip().split()
        if not command:
            continue

        cmd = command[0]

        if cmd == 'add-user' and len(command) == 2:
            manager.add_user(command[1])
        elif cmd == 'add-shopping-list' and len(command) == 3:
            manager.add_shopping_list(int(command[1]), command[2])
        elif cmd == 'add-item' and len(command) == 4:
            manager.add_item(int(command[1]), command[2], int(command[3]))
        elif cmd == 'list-users':
            manager.list_users()
        elif cmd == 'list-shopping-lists' and len(command) == 2:
            manager.list_shopping_lists(int(command[1]))
        elif cmd == 'list-items' and len(command) == 2:
            manager.list_items(int(command[1]))
        elif cmd == 'remove-item' and len(command) == 2:
            manager.remove_item(int(command[1]))
        elif cmd == 'list-tables':
            manager.list_tables()
        elif cmd == 'exit':
            print("Exiting...")
            break
        else:
            print("Invalid command. Please try again.")
            manager.display_help()

if __name__ == '__main__':
    main()