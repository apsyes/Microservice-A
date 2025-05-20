from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
DB_FILE = "restaurant.db"

@app.route('/get-restaurant', methods=['GET'])
def get_restaurant():
    try:
        hour = int(request.args.get('time', ''))
        if not (0 <= hour <= 24):
            raise ValueError
    except ValueError:
        return jsonify({"error": "Invalid 'time' value. Must be 0–24"}), 400

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute('''
        SELECT restaurant_Name, phone, foodType, openHour, closeHour
        FROM Restaurant
        WHERE is_Open = 1 AND openHour <= ? AND closeHour > ?
    ''', (hour, hour))

    rows = cursor.fetchall()
    conn.close()

    restaurants = [
        {
            "name": row[0],
            "phone": row[1],
            "type": row[2],
            "openHour": row[3],
            "closeHour": row[4]
        }
        for row in rows
    ]

    return jsonify(restaurants)

if __name__ == '__main__':
    app.run(debug=True, port=5001)