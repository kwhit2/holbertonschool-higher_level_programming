#!/usr/bin/python3
""" script that lists all cities from the database hbtn_0e_4_usa """


if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    conn = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name FROM cities INNER
                JOIN states ON cities.state_id = states.id ORDER BY
                id ASC""")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
