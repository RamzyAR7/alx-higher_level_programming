#!/usr/bin/python3
"""
this model for  lists all states from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb


def main():
    """ main funcion """
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cur = conn.cursor()
    query = """
            SELECT cities.name
            FROM cities
            INNER JOIN states ON states.id=cities.state_id
            WHERE states.name = %s
            """
    cur.execute(query, (sys.argv[4],))

    res = cur.fetchall()

    print(", ".join([city[0] for city in res]))

    conn.commit()
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
