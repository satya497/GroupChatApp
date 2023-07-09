![Screenshot (292)](https://github.com/satya497/GroupChatApp/assets/51437221/96f1b793-aff8-4ab8-9862-ee8a41cb1ad3)

# Chat App

This is a Flask-based chat application that allows users to create users, edit users, login/logout, create groups, send messages, and perform other related actions. The application uses MySQL as the database for storing user and message data.

## Key Features

- User management: Create new users, edit user details, and assign user roles.
- Authentication and authorization: Users can log in and log out, and certain actions are restricted based on user roles (admin/user).
- Group management: Create new groups and delete existing groups.
- Messaging: Users can send messages in specific groups and like messages.

## Requirements

- Python 3.x
- Flask
- MySQL Connector

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/yourusername/chat-app.git
   cd chat-app
   ```

2. Create a virtual environment:

   ```shell
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required dependencies:

   ```shell
   pip install -r requirements.txt
   ```

4. Configure the MySQL database:

   - Create a new MySQL database for the chat app.
   - Update the database connection details in the `db.py` file.

5. Start the application:

   ```shell
   python app.py
   ```

   The application will run on `http://localhost:5000`.

## Usage

1. Access the application in your web browser at `http://localhost:5000`.

2. Use the provided forms and UI to perform various actions such as creating users, editing users, logging in/out, creating groups, sending messages, and more.

## Code Explanation

The code is organized as follows:

- `app.py`: This is the main Flask application file that defines the routes and implements the actions of the chat app.
- `db.py`: This file contains the database connection setup and functions for executing database queries.
- `templates/`: This directory contains the HTML templates for rendering the UI.
- `static/`: This directory contains the CSS and JavaScript files for styling and client-side functionality.

The code includes decorator functions (`admin_required` and `login_required`) to handle authentication and authorization for certain routes. It also includes helper functions to retrieve user and group details from the database.

## Helper Functions:

- `get_user_id` : Retrieves the user ID from the request based on the username. It queries the database to find the corresponding user ID.
- `get_group_id`: Retrieves the group ID from the database based on the group name.
- `get_user_role`: Retrieves the user's role from the database based on the user ID.
- `get_message_id`: Retrieves the message ID from the database based on the message, user ID, and group ID.
- `is_authenticated`: Checks if the user is authenticated by verifying the user's state (e.g., "login") in the database.
- `update_user_state`: Updates the user's state in the user table of the database.

The routes in the application correspond to different actions and functionalities, such as creating users, editing users, login/logout, creating groups, sending messages, and more. The routes perform the necessary database operations (e.g., INSERT, UPDATE, DELETE, SELECT) and return responses in JSON format.

Please note that the code assumes the existence of a MySQL database with the required tables (`users`, `groups`, `messages`). Make sure to configure the database connection details in the `db.py` file and modify the SQL queries according to your specific database structure.

## Contributing

Contributions to this project are welcome. Here are some ways you can contribute:

- Report bugs and issues.
- Suggest new features or enhancements.
- Submit pull requests to improve the code.


## Acknowledgments

- The Flask framework and MySQL Connector library.

## Sample Outputs
![Uploading Screenshot (291).png…]()
![Uploading Screenshot (290).png…]()
![Screenshot (289)](https://github.com/satya497/GroupChatApp/assets/51437221/c809f82a-883e-44fe-9512-5141e8b2b544)
![Screenshot (293)](https://github.com/satya497/GroupChatApp/assets/51437221/b2a44fe4-4b54-42f3-b69d-3a163c74beec)
![Screenshot (287)](https://github.com/satya497/GroupChatApp/assets/51437221/24aaa94b-d8de-453e-8741-5d7ff996f815)
![Uploading Screenshot (286).png…]()
