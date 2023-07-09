from flask import Flask, render_template, request, jsonify
import mysql.connector
from db import db
app = Flask(__name__)


# Decorator function to check if the user is an admin
def admin_required(f):
    def decorator_function(*args, **kwargs):
        # Retrieve the user ID or token from the request and check if the user is an admin
        user_id = get_user_id(request)
        role = get_user_role(user_id)
        if role != "admin":
            return jsonify({"message": "Admin access required"})

        return f(*args, **kwargs)

    # Change the name of the decorated function to avoid duplication
    decorator_function.__name__ = f.__name__
    decorator_function.__doc__ = f.__doc__
    return decorator_function

# Decorator function to check if the user is authenticated
def login_required(f):
    def decorated_function(*args, **kwargs):
        # Retrieve the user ID or token from the request and check if the user is authenticated
        user_id = get_user_id(request)
        if not is_authenticated(user_id):
            return jsonify({"message": "Authentication required"})

        return f(*args, **kwargs)

    # Change the name and docstring of the decorated function to avoid duplication
    decorated_function.__name__ = f.__name__
    decorated_function.__doc__ = f.__doc__
    return decorated_function


# Helper function to retrieve the user ID from the request
def get_user_id(request):
    # Retrieve the username from the request (e.g., from headers, tokens, or session)
    username = request.json.get("username")  # Modify this line based on your request data

    # Fetch the user ID from the database based on the username
    cursor = db.cursor()
    sql = "SELECT user_id FROM users WHERE username = %s"
    val = (username,)
    cursor.execute(sql, val)
    result = cursor.fetchone()
    cursor.close()

    if result:
        return result[0]  # Return the user ID if found
    else:
        return None  # Return None if the user ID is not found

def get_group_id(group_name):
    # Retrieve group_id from the database based on group_name
    cursor = db.cursor()
    sql = "SELECT group_id FROM `groups` WHERE group_name = %s"
    val = (group_name,)
    cursor.execute(sql, val)
    result = cursor.fetchone()
    cursor.close()

    if result:
        return result[0]  # Return the group_id if found
    else:
        return None  # Return None if the group_id is not found


# Helper function to retrieve the user role from the database
def get_user_role(user_id):
    # Implement the logic to retrieve the user role from the database based on the user ID
    # Return the user role or None if not found
    cursor = db.cursor()
    sql = "SELECT role FROM users WHERE user_id = %s"
    val = (user_id,)
    cursor.execute(sql, val)
    result = cursor.fetchone()
    cursor.close()
    if result:
        return result[0]
    return None

def get_message_id(message, user_id, group_id):
    # Retrieve message_id from the database based on message and username
    cursor = db.cursor()
    sql = "SELECT message_id FROM messages WHERE message = %s AND user_id = %s AND group_id = %s"
    val = (message, user_id, group_id)
    cursor.execute(sql, val)
    result = cursor.fetchone()
    cursor.close()

    if result:
        return result[0]  # Return the message_id if found
    else:
        return None  # Return None if the message_id is not found


# Helper function to check if the user is authenticated
def is_authenticated(user_id):
    # Retrieve user details from the database
    cursor = db.cursor()
    sql = "SELECT * FROM users WHERE user_id = %s"
    val = (user_id,)
    cursor.execute(sql, val)
    user = cursor.fetchone()
    print(f'user is {user[3]} and state is {user[4]}')
    cursor.close()

    if user and user[4] == "login":
        # User exists in the database and the state is "login", indicating authentication
        return True
    else:
        # User does not exist in the database or the state is not "login", indicating authentication failure
        return False

# Function to update the user's state in the user table
def update_user_state(user_id, state):
    cursor = db.cursor()
    sql = "UPDATE users SET state = %s WHERE user_id = %s"
    val = (state, user_id)
    cursor.execute(sql, val)
    db.commit()
    cursor.close()


# Define a default route
@app.route('/')
def index():
    return render_template('index.html')

# Define routes for admin API
@app.route("/admin/create_user", methods=["POST"])
@admin_required
def create_user():
    # Retrieve user details from the request
    username = request.json.get("username")
    password = request.json.get("password")
    role = request.json.get("role", "user")  # Add a role field in the request
    user_details = request.json.get("user_details", {})
    new_user = user_details.get("user","")
    pwd = user_details.get("pwd","")
    new_role = user_details.get("role","user")
    # Insert user details into the database
    cursor = db.cursor()
    sql = "INSERT INTO users (username, password, role) VALUES (%s, %s, %s)"  # Add role column in the query
    val = (new_user, pwd, new_role)  # Include the role value in the insert statement
    cursor.execute(sql, val)
    db.commit()
    cursor.close()

    return jsonify({"message": "User created successfully"})

@app.route("/admin/edit_user", methods=["PUT"])
@admin_required
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

# Define routes for auth API
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
        # Update the user's state to "login" in the user table
        user_id = get_user_id(request)
        update_user_state(user_id, "login")
        return jsonify({"message": "Login successful"})
    else:
        return jsonify({"message": "Invalid username or password"})

@app.route("/auth/logout", methods=["POST"])
def logout():
    # Retrieve the user ID from the request
    user_id = get_user_id(request)

    # Update the user's state to "logout" in the user table
    update_user_state(user_id, "logout")

    return jsonify({"message": "Logout successful"})


# Define routes for group API
@app.route("/groups/create_group", methods=["POST"])
@login_required
def create_group():
    # Retrieve group details from the request
    group_name = request.json.get("group_name")
    group_id = get_group_id(group_name)
    # Check if the group with the given name already exists
    cursor = db.cursor()
    sql = "SELECT * FROM `groups` WHERE group_id = %s"
    val = (group_id,)
    cursor.execute(sql, val)
    existing_group = cursor.fetchall()  # Consume the result using fetchall()

    if existing_group:
        cursor.close()
        return jsonify({"message": f"Group '{group_name}' already exists"})

    # Insert group details into the database
    sql = "INSERT INTO `groups` (group_name) VALUES (%s)"
    val = (group_name,)
    cursor.execute(sql, val)
    db.commit()
    cursor.close()

    return jsonify({"message": "Group created successfully"})


@app.route("/groups/delete_group", methods=["DELETE", "POST"])
@login_required
def delete_group():
    # Retrieve group details from the request
    group_name = request.json.get("group_name")
    group_id = get_group_id(group_name)
    # Delete group from the database
    cursor = db.cursor()
    sql = "DELETE FROM `groups` WHERE group_id = %s"
    val = (group_id,)
    cursor.execute(sql, val)
    db.commit()
    cursor.close()

    return jsonify({"message": "Group deleted successfully"})

@app.route("/groups/search_groups", methods=["GET"])
@login_required
def search_groups():
    # Retrieve search query from the request
    search_query = request.json.get("group_name")

    # Perform search query in the groups table
    cursor = db.cursor()
    sql = "SELECT * FROM `groups` WHERE group_name LIKE %s"
    val = ('%' + search_query + '%',)
    cursor.execute(sql, val)
    groups = cursor.fetchall()
    cursor.close()

    return jsonify({"groups": groups})

# Define routes for message API
@app.route("/messages/send_message", methods=["POST"])
@login_required
def send_message():
    # Retrieve message details from the request
    message = request.json.get("message")
    group_name = request.json.get("group_name")
    group_id = get_group_id(group_name)
    user_id = get_user_id(request)
    # ... (other message details)

    # Insert message details into the database
    cursor = db.cursor()
    sql = "INSERT INTO messages (message, group_id, user_id) VALUES (%s, %s, %s)"
    val = (message, group_id, user_id)
    cursor.execute(sql, val)
    db.commit()
    cursor.close()

    return jsonify({"message": "Message sent successfully"})

@app.route("/messages/like_message", methods=["POST"])
@login_required
def like_message():
    # Retrieve message details from the request
    message = request.json.get("message")
    username = request.json.get("username")
    group_name = request.json.get("group_name")
    group_id = get_group_id(group_name)
    user_id = get_user_id(request)
    message_id = get_message_id(message, user_id, group_id)
    # Update message likes in the database
    cursor = db.cursor()
    sql = "UPDATE messages SET likes = likes + 1 WHERE message_id = %s AND user_id = %s"
    val = (message_id, user_id)
    cursor.execute(sql, val)
    db.commit()
    cursor.close()

    return jsonify({"message": "Message liked successfully"})


if __name__ == '__main__':
    app.run()
