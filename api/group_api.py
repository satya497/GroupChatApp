from flask import Flask, request, jsonify
from db import db

app = Flask(__name__)


@app.route("/groups/create_group", methods=["POST"])
def create_group():
    # Retrieve group details from the request
    group_name = request.json.get("group_name")
    # ... (other group details)

    # Insert group details into the database
    cursor = db.cursor()
    sql = "INSERT INTO groups (group_name) VALUES (%s)"
    val = (group_name,)
    cursor.execute(sql, val)
    db.commit()
    cursor.close()

    return jsonify({"message": "Group created successfully"})

@app.route("/groups/delete_group", methods=["DELETE"])
def delete_group():
    # Retrieve group details from the request
    group_id = request.json.get("group_id")

    # Delete group from the database
    cursor = db.cursor()
    sql = "DELETE FROM groups WHERE group_id = %s"
    val = (group_id,)
    cursor.execute(sql, val)
    db.commit()
    cursor.close()

    return jsonify({"message": "Group deleted successfully"})

# Implement other group-related endpoints (search groups, add members) here...

if __name__ == '__main__':
    app.run()
