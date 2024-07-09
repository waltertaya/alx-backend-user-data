# Basic Authentication Project

## Overview
This project involves learning the basics of authentication processes and implementing a Basic Authentication mechanism on a simple API. While it is recommended to use established modules or frameworks for Basic Authentication in a professional setting, this project aims to build a deep understanding by implementing the mechanism from scratch.

## Learning Objectives
By the end of this project, you should be able to:
- Explain the concept of authentication.
- Describe Base64 encoding and its applications.
- Encode a string using Base64.
- Understand and implement Basic Authentication.
- Send an Authorization header in HTTP requests.

## Requirements
### Python Scripts
- All scripts will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7.
- All files should end with a new line.
- The first line of all files should be `#!/usr/bin/env python3`.
- A README.md file at the root of the project is mandatory.
- Code should adhere to the pycodestyle style guide (version 2.5).
- All files must be executable.
- The length of the files will be tested using `wc`.
- All modules should have documentation.
- All classes should have documentation.
- All functions should have documentation.

## Tasks

### Task 0: Simple Basic API
- **Setup**: Download and start the project from the provided archive.
- **Start the server**: 
  ```bash
  pip3 install -r requirements.txt
  API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
  ```
- **Use the API**:
  ```bash
  curl "http://0.0.0.0:5000/api/v1/status" -vvv
  ```

### Task 1: Error handler for Unauthorized requests
- **Goal**: Implement a 401 error handler that returns `{"error": "Unauthorized"}` in JSON format.
- **Route**: `GET /api/v1/unauthorized`

### Task 2: Error handler for Forbidden requests
- **Goal**: Implement a 403 error handler that returns `{"error": "Forbidden"}` in JSON format.
- **Route**: `GET /api/v1/forbidden`

### Task 3: Auth Class
- **Create**: A class `Auth` in `api/v1/auth/auth.py` to manage API authentication with methods:
  - `require_auth`
  - `authorization_header`
  - `current_user`

### Task 4: Define routes that don’t need authentication
- **Update**: `require_auth` method in `Auth` class to handle excluded paths.

### Task 5: Request validation
- **Update**: `authorization_header` method in `Auth` class to validate requests.
- **Implement**: `before_request` handler in `api/v1/app.py` to filter each request based on authentication.

### Task 6: Basic Auth Class
- **Create**: A class `BasicAuth` that inherits from `Auth`.
- **Update**: `api/v1/app.py` to use `BasicAuth` based on the environment variable `AUTH_TYPE`.

### Task 7: Extract Base64 part
- **Add**: `extract_base64_authorization_header` method in `BasicAuth` class to return the Base64 part of the Authorization header.

### Task 8: Decode Base64
- **Add**: `decode_base64_authorization_header` method in `BasicAuth` class to decode Base64 strings.

### Task 9: Extract User Credentials
- **Add**: `extract_user_credentials` method in `BasicAuth` class to return user email and password from the Base64 decoded value.

### Task 10: User Object from Credentials
- **Add**: `user_object_from_credentials` method in `BasicAuth` class to return the User instance based on email and password.

### Task 11: Overload current_user
- **Complete**: The `current_user` method in `BasicAuth` class to return the User instance for the current authenticated user.

### Tasks

12. **Basic - Allow password with `:`**
   Improve the method `extract_user_credentials(self, decoded_base64_authorization_header)` to allow passwords containing `:`.

   **Example:**
   ```bash
   bob@dylan:~$ cat main_100.py
   #!/usr/bin/env python3
   """ Main 100 """
   import base64
   from api.v1.auth.basic_auth import BasicAuth
   from models.user import User

   """ Create a user test """
   user_email = "bob100@hbtn.io"
   user_clear_pwd = "H0lberton:School:98!"

   user = User()
   user.email = user_email
   user.password = user_clear_pwd
   print("New user: {}".format(user.id))
   user.save()

   basic_clear = "{}:{}".format(user_email, user_clear_pwd)
   print("Basic Base64: {}".format(base64.b64encode(basic_clear.encode('utf-8')).decode("utf-8")))

   bob@dylan:~$ 
   bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 ./main_100.py 
   New user: 5891469b-d2d5-4d33-b05d-02617d665368
   Basic Base64: Ym9iMTAwQGhidG4uaW86SDBsYmVydG9uOlNjaG9vbDo5OCE=
   bob@dylan:~$
   bob@dylan:~$ API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=basic_auth python3 -m api.v1.app
   * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
   ```

   **In a second terminal:**
   ```bash
   bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/status"
   {
     "status": "OK"
   }
   bob@dylan:~$
   bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/users"
   {
     "error": "Unauthorized"
   }
   bob@dylan:~$ 
   bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Test"
   {
     "error": "Forbidden"
   }
   bob@dylan:~$
   bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Basic test"
   {
     "error": "Forbidden"
   }
   bob@dylan:~$
   bob@dylan:~$ curl "http://0.0.0.0:5000/api/v1/users" -H "Authorization: Basic Ym9iMTAwQGhidG4uaW86SDBsYmVydG9uOlNjaG9vbDo5OCE="
   [
     {
       "created_at": "2017-09-25 01:55:17", 
       "email": "bob@hbtn.io", 
       "first_name": null, 
       "id": "9375973a-68c7-46aa-b135-29f79e837495", 
       "last_name": null, 
       "updated_at": "2017-09-25 01:55:17"
     },
     {
       "created_at": "2017-09-25 01:59:42", 
       "email": "bob100@hbtn.io", 
       "first_name": null, 
       "id": "5891469b-d2d5-4d33-b05d-02617d665368", 
       "last_name": null, 
       "updated_at": "2017-09-25 01:59:42"
     }
   ]
   bob@dylan:~$
   ```

   **Repo:**
   - GitHub repository: `alx-backend-user-data`
   - Directory: `0x01-Basic_authentication`
   - File: `api/v1/auth/basic_auth.py`

13. **Require auth with stars**
   Improve `def require_auth(self, path, excluded_paths)` by allowing `*` at the end of excluded paths.

   **Example for `excluded_paths = ["/api/v1/stat*"]`:**
   - `/api/v1/users` will return `True`
   - `/api/v1/status` will return `False`
   - `/api/v1/stats` will return `False`

   **Repo:**
   - GitHub repository: `alx-backend-user-data`
   - Directory: `0x01-Basic_authentication`
   - File: `api/v1/auth/auth.py`

## Repository
- **GitHub Repository**: `alx-backend-user-data`
- **Directory**: `0x01-Basic_authentication`

## Usage
To run the project, set up the environment and start the server:
```bash
export API_HOST=0.0.0.0
export API_PORT=5000
python3 -m api.v1.app
```

## Testing
To test the different endpoints and functionalities, use `curl` commands or any API testing tool like Postman.

# Simple API

Simple HTTP API for playing with `User` model.


## Files

### `models/`

- `base.py`: base of all models of the API - handle serialization to file
- `user.py`: user model

### `api/v1`

- `app.py`: entry point of the API
- `views/index.py`: basic endpoints of the API: `/status` and `/stats`
- `views/users.py`: all users endpoints


## Setup

```
$ pip3 install -r requirements.txt
```


## Run

```
$ API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
```


## Routes

- `GET /api/v1/status`: returns the status of the API
- `GET /api/v1/stats`: returns some stats of the API
- `GET /api/v1/users`: returns the list of users
- `GET /api/v1/users/:id`: returns an user based on the ID
- `DELETE /api/v1/users/:id`: deletes an user based on the ID
- `POST /api/v1/users`: creates a new user (JSON parameters: `email`, `password`, `last_name` (optional) and `first_name` (optional))
- `PUT /api/v1/users/:id`: updates an user based on the ID (JSON parameters: `last_name` and `first_name`)
