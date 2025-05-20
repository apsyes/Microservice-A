import sqlite3

conn = sqlite3.connect('restaurant.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Restaurant (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    restaurant_Name TEXT,
    phone TEXT,
    foodType TEXT,
    openHour INTEGER,
    closeHour INTEGER,
    is_Open INTEGER
);
''')

cursor.executemany('''
INSERT INTO Restaurant(restaurant_Name, phone, foodType, openHour, closeHour, is_Open)
VALUES (?, ?, ?, ?, ?, ?)
''', [
    ("Luigi’s Pizza", "5551234", "Pizza", 11, 23, 1),
    ("Sushi Samurai", "5552234", "Japanese", 12, 22, 0),
    ("Burger Bomb", "5553234", "Fast Food", 10, 21, 1),
    ("Curry Castle", "5554234", "Indian", 11, 22, 1),
    ("Taco Tempest", "5555234", "Mexican", 10, 20, 0),
    ("Pho Paradise", "5556234", "Vietnamese", 10, 22, 1),
    ("Steak Street", "5557234", "Steakhouse", 17, 23, 1),
    ("Vegan Valley", "5558234", "Vegan", 9, 20, 1),
    ("Waffle World", "5559234", "Breakfast", 7, 15, 1),
    ("Dim Sum Delights", "5560234", "Chinese", 10, 16, 1)
])

conn.commit()
conn.close()
print("Database setup complete.")
