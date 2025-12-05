import sqlite3


def create_database():
    conn = sqlite3.connect("phonebook.db")
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS Entries (
            Name TEXT PRIMARY KEY,
            Phone TEXT
        )
    """)

    conn.commit()
    conn.close()

def add_entry():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")

    conn = sqlite3.connect("phonebook.db")
    cur = conn.cursor()

    try:
        cur.execute("INSERT INTO Entries (Name, Phone) VALUES (?, ?)", (name, phone))
        conn.commit()
        print("Entry added successfully.")
    except sqlite3.IntegrityError:
        print("That name already exists in the phonebook.")

    conn.close()

def lookup_entry():
    name = input("Enter name to look up: ")

    conn = sqlite3.connect("phonebook.db")
    cur = conn.cursor()

    cur.execute("SELECT Phone FROM Entries WHERE Name = ?", (name,))
    result = cur.fetchone()

    if result:
        print(f"{name}'s phone number is: {result[0]}")
    else:
        print("Name not found.")

    conn.close()

def update_entry():
    name = input("Enter name to update: ")
    new_phone = input("Enter new phone number: ")

    conn = sqlite3.connect("phonebook.db")
    cur = conn.cursor()

    cur.execute("UPDATE Entries SET Phone = ? WHERE Name = ?", (new_phone, name))
    conn.commit()

    if cur.rowcount == 0:
        print("Name not found — no changes made.")
    else:
        print("Phone number updated.")

    conn.close()

def delete_entry():
    name = input("Enter name to delete: ")

    conn = sqlite3.connect("phonebook.db")
    cur = conn.cursor()

    cur.execute("DELETE FROM Entries WHERE Name = ?", (name,))
    conn.commit()

    if cur.rowcount == 0:
        print("Name not found — nothing deleted.")
    else:
        print("Entry deleted.")

    conn.close()

def display_menu():
    print("\n--- PHONEBOOK MENU ---")
    print("1. Add Entry")
    print("2. Look Up Phone Number")
    print("3. Update Phone Number")
    print("4. Delete Entry")
    print("5. Quit")

def main():
    create_database()

    while True:
        display_menu()
        choice = input("Enter your choice (1–5): ")

        if choice == "1":
            add_entry()
        elif choice == "2":
            lookup_entry()
        elif choice == "3":
            update_entry()
        elif choice == "4":
            delete_entry()
        elif choice == "5":
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Please enter 1–5.")

if __name__ == "__main__":
    main()