import requests
import pandas as pd

# Connecting to an API
url = 'https://api.example.com/data'
response = requests.get(url)
data = response.json()
df = pd.DataFrame(data)

# Reading data from a database
import sqlite3

conn = sqlite3.connect('database.db')
df = pd.read_sql_query("SELECT * FROM table_name", conn)
