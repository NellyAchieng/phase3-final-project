import sqlite3

class ShoppingListManager:
    def _init_(self):
        
        pass
    @classmethod
    def create_tables(cls):
        with sqlite3.connect("cli.db") as conn:
            cursor = conn.cursor()
            sql='''CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL
            )'''
            cursor.execute(sql)
            sql1='''CREATE TABLE IF NOT EXISTS shopping_lists (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                user_id INTEGER NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )'''
            cursor.execute(sql1)
            sql2='''CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                shopping_list_id INTEGER NOT NULL,
                FOREIGN KEY (shopping_list_id) REFERENCES shopping_lists (id)
            )'''
            cursor.execute(sql2)
            conn.commit()

    def add_user(self, name):
        with sqlite3.connect("cli.db") as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO users (name) VALUES (?)', (name,))
            conn.commit()
        print(f"User {name} added.")

    def list_users(self):
        with sqlite3.connect("cli.db") as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT id, name FROM users')
            users = cursor.fetchall()
            if not users:
                print("No users available.")
                return
            for user in users:
                print(f"ID: {user[0]}, Name: {user[1]}")

    def add_shopping_list(self, user_id, name):
        with sqlite3.connect("cli.db") as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO shopping_lists (name, user_id) VALUES (?, ?)', (name, user_id))
            conn.commit()
        print(f"Shopping list {name} added for user ID {user_id}.")

    def list_shopping_lists(self, user_id):
        with sqlite3.connect("cli.db") as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT id, name FROM shopping_lists WHERE user_id = ?', (user_id,))
            shopping_lists = cursor.fetchall()
            if not shopping_lists:
                print(f"No shopping lists found for user ID {user_id}.")
                return
            for shopping_list in shopping_lists:
                print(f"ID: {shopping_list[0]}, Name: {shopping_list[1]}")

    def add_item(self, shopping_list_id, name, quantity):
        with sqlite3.connect("cli.db") as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO items (name, quantity, shopping_list_id) VALUES (?, ?, ?)', (name, quantity, shopping_list_id))
            conn.commit()
        print(f"Item {name} with quantity {quantity} added to shopping list ID {shopping_list_id}.")

    def list_items(self, shopping_list_id):
        with sqlite3.connect("cli.db") as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT id, name, quantity FROM items WHERE shopping_list_id = ?', (shopping_list_id,))
            items = cursor.fetchall()
            if not items:
                print(f"No items found for shopping list ID {shopping_list_id}.")
                return
            for item in items:
                print(f"ID: {item[0]}, Name: {item[1]}, Quantity: {item[2]}")

    def remove_item(self, item_id):
        with sqlite3.connect("cli.db") as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM items WHERE id = ?', (item_id,))
            conn.commit()
        print(f"Item with ID {item_id} removed.")

    def list_tables(self):
        with sqlite3.connect("cli.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cursor.fetchall()
            if not tables:
                print("No tables found.")
                return
            print("Tables in the database:")
            for table in tables:
                print(table[0])

    def display_help(self):
        help_text = """
        Available commands:
        1. Add User: add-user [name]
        2. Add Shopping List: add-shopping-list [user_id] [name]
        3. Add Item: add-item [shopping_list_id] [name] [quantity]
        4. List Users: list-users
        5. List Shopping Lists: list-shopping-lists [user_id]
        6. List Items: list-items [shopping_list_id]
        7. Remove Item: remove-item [item_id]
        8. List Tables: list-tables
        9. Exit: exit
        """
        print(help_text)
        
ShoppingListManager.create_tables()
