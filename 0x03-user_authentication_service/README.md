# User Authentication Service

## Overview

This project involves creating a user authentication service using Flask, SQLAlchemy, and bcrypt for hashing passwords. The service includes creating user models, handling user sessions, and implementing secure password handling. The objective is to gain a thorough understanding of the mechanisms involved in user authentication by building the service from scratch.


## Requirements

- Editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7.
- Files should end with a new line.
- The first line of all files should be exactly `#!/usr/bin/env python3`.
- A `README.md` file is mandatory.
- Code should follow the `pycodestyle` style (version 2.5).
- Use SQLAlchemy 1.3.x.
- All files must be executable.
- Modules, classes, and functions should have proper documentation.
- Functions should be type annotated.
- The Flask app should only interact with Auth and never directly with the DB.

## Setup

To get started, you need to install bcrypt:

```bash
pip3 install bcrypt
```

## Tasks

### 0. User Model

Create a SQLAlchemy model named `User` for a database table named `users`. The model should have the following attributes:

- `id`: Integer primary key
- `email`: Non-nullable string
- `hashed_password`: Non-nullable string
- `session_id`: Nullable string
- `reset_token`: Nullable string

### 1. Create User

Implement the `add_user` method in the `DB` class. This method should:

- Take two string arguments: `email` and `hashed_password`.
- Return a `User` object.
- Save the user to the database.

### 2. Find User

Implement the `find_user_by` method in the `DB` class. This method should:

- Take arbitrary keyword arguments.
- Return the first row found in the `users` table as filtered by the input arguments.
- Raise `NoResultFound` and `InvalidRequestError` as appropriate.

### 3. Update User

Implement the `update_user` method in the `DB` class. This method should:

- Take a required `user_id` integer and arbitrary keyword arguments.
- Use `find_user_by` to locate the user to update.
- Update the user's attributes as passed in the method’s arguments.
- Commit changes to the database.
- Raise a `ValueError` for invalid arguments.

### 4. Hash Password

Define a `_hash_password` method that:

- Takes a password string argument.
- Returns a salted hash of the input password, hashed with `bcrypt.hashpw`.

### 5. Register User

Implement the `Auth.register_user` method. This method should:

- Take mandatory `email` and `password` string arguments.
- Return a `User` object.
- Raise a `ValueError` if the user already exists.
- Hash the password and save the user to the database.

### 6. Basic Flask App

Set up a basic Flask app with a single GET route ("/") that returns a JSON payload:

```json
{"message": "Bienvenue"}
```

### 7. Register User Endpoint

Implement the `/users` POST route to register a user. The endpoint should:

- Expect form data fields: `email` and `password`.
- Register the user if they do not exist and respond with a JSON payload.
- Return a 400 status code if the user is already registered.

### 8. Credentials Validation

Implement the `Auth.valid_login` method. This method should:

- Expect `email` and `password` required arguments.
- Return a boolean indicating if the login is valid.

### 9. Generate UUIDs

Implement a `_generate_uuid` function that returns a string representation of a new UUID using the `uuid` module.

### 10. Get Session ID

Implement the `Auth.create_session` method. This method should:

- Take an `email` string argument.
- Return the session ID as a string.

### 11. Log In

Implement a login function for the POST `/sessions` route. This function should:

- Expect form data with `email` and `password`.
- Create a new session for the user if the login is valid.
- Store the session ID as a cookie and return a JSON payload.

### 12. Find User by Session ID

Implement the `Auth.get_user_from_session_id` method. This method should:

- Take a `session_id` string argument.
- Return the corresponding `User` or `None`.

### 13. Destroy Session

Implement the `Auth.destroy_session` method. This method should:

- Take a `user_id` integer argument.
- Update the corresponding user's session ID to `None`.

### 14. Log Out

Implement a logout function for the DELETE `/sessions` route. This function should:

- Find the user with the requested session ID.
- Destroy the session and redirect the user to GET `/`.

### 15. User Profile

Implement a profile function for the GET `/profile` route. This function should:

- Expect a `session_id` cookie.
- Respond with the user's email if the session ID is valid.
- Return a 403 status code if the session ID is invalid or the user does not exist.

## Repository Structure

```plaintext
alx-backend-user-data/
├── 0x03-user_authentication_service/
│   ├── user.py
│   ├── db.py
│   ├── auth.py
│   ├── app.py
│   ├── README.md
```

## Authors

- [@waltertaya](https://github.com/waltertaya)
