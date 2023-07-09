from flask import Flask, request, jsonify
from db import db

app = Flask(__name__)

@app.route("/auth/login", methods=["POST"])
def login():
    # Retrieve credentials from the request
    username = request.json.get("username")
    password = request.json.get("password")

    # Verify credentials against the database
    cursor = db.cursor()
    sql = "SELECT * FROM users WHERE username = %s AND password = %s"
    val = (username, password)
    cursor.execute(sql, val)
    user = cursor.fetchone()
    cursor.close()

    if user:
        return jsonify({"message": "Login successful"})
    else:
        return jsonify({"message": "Invalid username or password"})

@app.route("/auth/logout", methods=["POST"])
def logout():
    # Need Implementation for user logout
    # Clear user session or token

    return jsonify({"message": "Logout successful"})

if __name__ == '__main__':
    app.run()
