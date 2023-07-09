from flask import Flask, request, jsonify
from db import db

admin_api = Flask(__name__)


@admin_api.route("/admin/create_user", methods=["POST"])
def create_user():
    # Retrieve user details from the request
    username = request.json.get("username")
    password = request.json.get("password")
    # ... (other user details)

    # Insert user details into the database
    cursor = db.cursor()
    sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
    val = (username, password)
    cursor.execute(sql, val)
    db.commit()
    cursor.close()

    return jsonify({"message": "User created successfully"})

@admin_api.route("/admin/edit_user", methods=["PUT"])
def edit_user():
    # Retrieve user details from the request
    user_id = request.json.get("user_id")
    new_username = request.json.get("new_username")
    # ... (other user details to edit)

    # Update user details in the database
    cursor = db.cursor()
    sql = "UPDATE users SET username = %s WHERE user_id = %s"
    val = (new_username, user_id)
    cursor.execute(sql, val)
    db.commit()
    cursor.close()

    return jsonify({"message": "User updated successfully"})

if __name__ == '__main__':
    admin_api.run()
