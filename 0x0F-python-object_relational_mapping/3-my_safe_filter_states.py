#!/usr/bin/python3
""" LIKE TASK 2 BUT MORE SECURE SO USE THIS WAY: script that takes in an...
    ...argument and displays all values in the states table of hbtn_0e_0_usa...
    where name matches the argument. """


if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    conn = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("""SELECT * FROM states WHERE name=%s ORDER BY
                id ASC""", (argv[4],))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
