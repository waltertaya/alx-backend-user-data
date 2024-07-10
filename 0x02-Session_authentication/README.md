# Session Authentication Project

## Background Context
In this project, you will implement Session Authentication. For learning purposes, we will walk through each step of this mechanism instead of using a pre-built module or framework. This will help you understand the inner workings of session authentication.

## Resources
Read or watch:
- REST API Authentication Mechanisms - Only the session auth part
- HTTP Cookie
- Flask
- Flask Cookie


## Requirements
### Python Scripts
- All files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7).
- All files should end with a new line.
- The first line of all your files should be exactly `#!/usr/bin/env python3`.
- A `README.md` file at the root of the project folder is mandatory.
- Your code should use the `pycodestyle` style (version 2.5).
- All files must be executable.
- The length of your files will be tested using `wc`.
- All modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`).
- All classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`).
- All functions (inside and outside a class) should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`).

## Tasks
### 0. Et moi et moi et moi!
- Copy all your work from the `0x06. Basic authentication` project into this new folder.
- Add a new endpoint: `GET /users/me` to retrieve the authenticated User object.
- Update `@app.before_request` in `api/v1/app.py`.
- Update method for the route `GET /api/v1/users/<user_id>` in `api/v1/views/users.py`.

### 1. Empty session
- Create a class `SessionAuth` that inherits from `Auth`.
- Validate if everything inherits correctly without any overloading.
- Validate the “switch” by using environment variables.
- Update `api/v1/app.py` to use `SessionAuth` instance for the variable `auth` depending on the value of the environment variable `AUTH_TYPE`.

### 2. Create a session
- Update `SessionAuth` class:
  - Create a class attribute `user_id_by_session_id` initialized by an empty dictionary.
  - Create an instance method `def create_session(self, user_id: str = None) -> str`.

### 3. User ID for Session ID
- Update `SessionAuth` class:
  - Create an instance method `def user_id_for_session_id(self, session_id: str = None) -> str`.

### 4. Session cookie
- Update `api/v1/auth/auth.py` by adding the method `def session_cookie(self, request=None)`.

### 5. Before request
- Update the `@app.before_request` method in `api/v1/app.py`.

### 6. Use Session ID for identifying a User
- Update `SessionAuth` class:
  - Create an instance method `def current_user(self, request=None)` (overload) that returns a User instance based on a cookie value.

## Repository
- GitHub repository: `alx-backend-user-data`
- Directory: `0x02-Session_authentication`
- Files: 
  - `api/v1/app.py`
  - `api/v1/views/users.py`
  - `api/v1/auth/session_auth.py`
  - `api/v1/auth/auth.py`

### Setup and Running Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/alx-backend-user-data.git
   ```
2. Navigate to the project directory:
   ```bash
   cd alx-backend-user-data/0x02-Session_authentication
   ```
3. Ensure all dependencies are installed.
4. Run the application:
   ```bash
   API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth SESSION_NAME=_my_session_id python3 -m api.v1.app
   ```

## Testing
1. In a terminal, create a new user and print the Session ID:
   ```bash
   API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=session_auth ./main_0.py
   ```
2. In another terminal, test various endpoints using `curl`:
   ```bash
   curl "http://0.0.0.0:5000/api/v1/status"
   curl "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Basic <base64_encoded_credentials>"
   curl "http://0.0.0.0:5000/api/v1/users/me" --cookie "_my_session_id=<session_id>"
   ```

## Author

- **@waltertaya**
