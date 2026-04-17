from connect import connect


def search_pattern():
    pattern = input("Enter search pattern: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM search_pattern(%s)", (pattern,))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


def upsert_user():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute("CALL upsert_user(%s, %s)", (name, phone))

    conn.commit()
    cur.close()
    conn.close()


def bulk_insert():
    n = int(input("How many users: "))

    names = []
    phones = []

    for _ in range(n):
        names.append(input("Name: "))
        phones.append(input("Phone: "))

    conn = connect()
    cur = conn.cursor()

    cur.execute("CALL bulk_insert(%s, %s)", (names, phones))

    conn.commit()
    cur.close()
    conn.close()


def get_paginated():
    limit = int(input("Limit: "))
    offset = int(input("Offset: "))

    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM get_paginated(%s, %s)", (limit, offset))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


def delete_user():
    value = input("Enter name or phone: ")

    conn = connect()
    cur = conn.cursor()

    cur.execute("CALL delete_user(%s)", (value,))

    conn.commit()
    cur.close()
    conn.close()


def menu():
    while True:
        print("\n1. Search pattern")
        print("2. Upsert user")
        print("3. Bulk insert")
        print("4. Pagination")
        print("5. Delete user")
        print("0. Exit")

        choice = input("Choose: ")

        if choice == "1":
            search_pattern()
        elif choice == "2":
            upsert_user()
        elif choice == "3":
            bulk_insert()
        elif choice == "4":
            get_paginated()
        elif choice == "5":
            delete_user()
        elif choice == "0":
            break


menu()
