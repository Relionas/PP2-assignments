import csv
from connect import connect

def insert_from_csv(filename):
    conn = connect()
    cur = conn.cursor()

    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            cur.execute(
                "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
                (row['name'], row['phone'])
            )

    conn.commit()
    cur.close()
    conn.close()
def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
        (name, phone)
    )

    conn.commit()
    cur.close()
    conn.close()
def update_contact(old_name):
    new_name = input("New name (leave blank to skip): ")
    new_phone = input("New phone (leave blank to skip): ")

    conn = connect()
    cur = conn.cursor()

    if new_name:
        cur.execute("UPDATE phonebook SET name=%s WHERE name=%s", (new_name, old_name))

    if new_phone:
        cur.execute("UPDATE phonebook SET phone=%s WHERE name=%s", (new_phone, old_name))

    conn.commit()
    cur.close()
    conn.close()
def search_by_name(name):
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM phonebook WHERE name ILIKE %s", ('%' + name + '%',))
    print(cur.fetchall())

    cur.close()
    conn.close()


def search_by_phone_prefix(prefix):
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM phonebook WHERE phone LIKE %s", (prefix + '%',))
    print(cur.fetchall())

    cur.close()
    conn.close()
def delete_contact(value):
    conn = connect()
    cur = conn.cursor()

    cur.execute("DELETE FROM phonebook WHERE name=%s OR phone=%s", (value, value))

    conn.commit()
    cur.close()
    conn.close()
def menu():
    while True:
        print("\n1. Insert CSV")
        print("2. Insert manually")
        print("3. Update contact")
        print("4. Search by name")
        print("5. Search by phone prefix")
        print("6. Delete contact")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == "1":
            insert_from_csv("contacts.csv")
        elif choice == "2":
            insert_from_console()
        elif choice == "3":
            name = input("Enter name to update: ")
            update_contact(name)
        elif choice == "4":
            name = input("Enter name: ")
            search_by_name(name)
        elif choice == "5":
            prefix = input("Enter prefix: ")
            search_by_phone_prefix(prefix)
        elif choice == "6":
            value = input("Enter name or phone to delete: ")
            delete_contact(value)
        elif choice == "0":
            break

menu()
