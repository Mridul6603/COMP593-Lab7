from faker import Faker
import sqlite3
import pandas as pd
import os
import csv


# Define an SQL query that inserts a row of data in the people table.
# The ?'s are placeholders to be fill in when the query is executed.
# Specific values can be passed as a tuple into the execute() method.
def main():

    con = sqlite3.connect('social_network.db')
    cur = con.cursor()
    query = "SELECT name, age FROM people WHERE age >= 50"
    cur.execute(query)
    all_people = cur.fetchall()
   
    con.close()
   
    for i in all_people:
        name = i[0]
        age = i[1]
        print(name, age)

        for i in all_people:
            print(f'{i[0]} is {i[1]} years old')
   
        path_of_csv = "output.csv"

        df = pd.DataFrame(all_people, columns=[{i[0]}, {i[1]}])
        df.to_csv(path_of_csv, index=False)


main()