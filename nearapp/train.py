import json
import psycopg2


import sqlite3

conn = sqlite3.connect('../db.sqlite3')


data = {
    "intents": [{
        "tag": "greeting",
        "patterns": [
            "Hi",
            "Hey",
            "How are you",
            "Is anyone there?",
            "Hello"
        ],
        "responses":[
            "Hey",
            "Hello",
            "Hi there",
            "Hi there, how can I help?"
        ]
    }]
}


def getCollege(id):
    cursorShop = conn.execute(
        "SELECT id,college_id, ShopName, address, AveragePrice ,Type from nearapp_college")

    return name


lst = data["intents"]

print(lst)
cursorShop = conn.execute(
    "SELECT id,college_id, ShopName, address, AveragePrice ,Type from nearapp_shop ORDER BY -AveragePrice")

for row in cursorShop:
    # print("ID = ", row[0])
    # print("College NAME = ", row[1])
    # print("Shop NAME = ", row[2])
    # print("ADDRESS = ", row[3])
    # print("SALARY = ", row[4], "\n")

    ent = {
        "tag": "nearby",
        "patterns": [
            f"Best {row[5]} near  {row[1]}"

        ],
        "responses": [
            "Hey",
            "Hello",
            "Hi there",
            "Hi there, how can I help?"
        ]
    }
    lst.append(ent)

print("Operation done successfully")
conn.close()

print(lst)
