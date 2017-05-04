#!/usr/bin/env python3
import psycopg2
import queries

DBNAME = "news"


def print_two_col_report(cursor: "Cursor to open DB", query: str="",
                         title: str="", unit: str="") -> None:
    """Print report with 2 columns of given `query`. Not suitable for results
    with more than 2 columns!
    
    Keyword arguments:
    cursor -- DB cursor object to open DB
    query -- SQL query as str
    title -- title of report as str
    unit -- optional unit for second column in report as str
    """
    cursor.execute(query)
    results = cursor.fetchall()

    print(title)
    for result in results:
        print("{} - {} {}".format(result[0], result[1], unit))
    print("")


def print_report():
    """Connect to `DBNAME` and print results from `queries`."""
    conn = psycopg2.connect(database=DBNAME)
    cur = conn.cursor()

    print("--- REPORT BEGIN ---\n")
    print_two_col_report(cur, queries.TOP_ARTICLES,
                         "Most popular 3 articles of all time:", "views")
    print_two_col_report(cur, queries.TOP_AUTHORS,
                         "Most popular authors of all time:", "views")
    print_two_col_report(cur, queries.ERROR_DATES,
                         "Days with more than 1% error rate:", "%")
    print("--- REPORT END ---")

    cur.close()
    conn.close()


if __name__ == "__main__":
    print_report()
