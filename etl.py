"""
Create a simple, and reusable ETL for Postgres databases
"""
import csv, sqlalchemy as sql
from sqlalchemy import create_engine
import psycopg2

# Define connection
engine = create_engine("postgresql+psycopg2://postgres:pass@/ETL_Test")

# Seed the users table w/ sample data from csv file
with open('data.csv', 'r') as data_file:
    reader = csv.reader(data_file)
    next(reader) # Skip header row
    for row in reader:
        engine.execute( # Parameterize query to avoid SQL injections
            "INSERT INTO users(email, lname, fname, homeaddress) VALUES(%s, %s, %s, %s)",
            row
        )

