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
    cur.execute("""SELECT *
                FROM states
                WHERE name = '{}'
                ORDER BY id ASC
                """.format(sys.argv[4]))

    res = cur.fetchall()
    for row in res:
        print(row)
    conn.commit()
    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
