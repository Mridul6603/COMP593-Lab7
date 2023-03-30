from faker import Faker
import sqlite3
from datetime import datetime
import pandas as pd


def query():

    con = sqlite3.connect('social_network.db')

    cur = con.cursor()  

    create_ppl_tbl_query = """
    CREATE TABLE IF NOT EXISTS people
    (
    ID INTEGER PRIMARY KEY,
    Name TEXT NOT NULL,
    Email TEXT NOT NULL,
    address TEXT NOT NULL,
    city TEXT NOT NULL,
    province TEXT NOT NULL,
    bio TEXT,
    age INTEGER,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL
    );
    """

    cur.execute(create_ppl_tbl_query)



    con.commit()

    return cur, con

def faker(cur):
   

    add_person_query = """
        INSERT INTO people
        (
        ID,
        name,
        email,
        address,
        city,
        province,
        bio,
        age,
        created_at,
        updated_at
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        """
# Define a tuple of data for the new person to insert into people table
# Data values must be in the same order as specified in query

    for i in range(1, 200):
        i = i + 1


        fake = Faker("en_CA")

        new_person = (
        i,
        fake.first_name(), # fake name
        fake.email(), # fake name
        fake.address(), # fake address
        fake.city(), #fake city
        fake.province(), # fake province
        fake.text(max_nb_chars=200), #fake bio
        fake.random_int(min=1, max=100), #fake age
        datetime.now(),
        datetime.now()) #current date and time as requested.

        # Execute query to add new person to people table

        cur.execute(add_person_query, new_person)


    con.commit()
cur, con = query()
faker(cur)
con.close()