from connect import connect

def call_search(pattern):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM search_pattern(%s)", (pattern,))
    print(cur.fetchall())
    cur.close()
    conn.close()

def call_upsert(name, phone):
    conn = connect()
    cur = conn.cursor()
    cur.execute("CALL upsert_user(%s, %s)", (name, phone))
    conn.commit()
    cur.close()
    conn.close()

def call_bulk_insert(users):
    conn = connect()
    cur = conn.cursor()
    cur.execute("CALL bulk_insert(%s)", (users,))
    conn.commit()
    cur.close()
    conn.close()

def call_delete(value):
    conn = connect()
    cur = conn.cursor()
    cur.execute("CALL delete_user(%s)", (value,))
    conn.commit()
    cur.close()
    conn.close()

def call_paginated(limit, offset):
    conn = connect()
    cur = conn.cursor()
    cur.execute("SELECT * FROM get_paginated(%s, %s)", (limit, offset))
    print(cur.fetchall())
    cur.close()
    conn.close()
