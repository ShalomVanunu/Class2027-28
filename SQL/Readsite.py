import requests
import sqlite3


url = 'https://jsonplaceholder.typicode.com/todos?_limit=5'
def read_site(url):
    data = requests.get(url).json()
    return data

print(read_site(url))