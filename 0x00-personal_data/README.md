# alx-backend-user-data

## Overview
This project focuses on managing and securing personal data using Python. It covers various aspects such as logging, password encryption, and secure database connections. The goal is to ensure that sensitive information, especially Personally Identifiable Information (PII), is handled and protected appropriately.


## Learning Objectives
By the end of this project, you should be able to:
- Identify examples of Personally Identifiable Information (PII).
- Implement a log filter to obfuscate PII fields.
- Encrypt passwords and verify the validity of input passwords.
- Authenticate to a database using environment variables.

## Requirements
- All files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7.
- Files must end with a new line.
- The first line of all files should be `#!/usr/bin/env python3`.
- A `README.md` file at the root of the project folder is mandatory.
- Code should follow the `pycodestyle` style (version 2.5).
- All files must be executable.
- File lengths will be tested using `wc`.
- All modules, classes, and functions must have documentation.
- Functions should be type annotated.

## Tasks

### 0. Regex-ing
**Objective:** Write a function `filter_datum` that returns the log message obfuscated.
- **File:** `filtered_logger.py`
- **Function:** `filter_datum(fields, redaction, message, separator)`

```python
def filter_datum(fields, redaction, message, separator):
    # Function implementation here
```

### 1. Log Formatter
**Objective:** Update the `RedactingFormatter` class to filter values in log records.
- **File:** `filtered_logger.py`
- **Class:** `RedactingFormatter`

```python
class RedactingFormatter(logging.Formatter):
    # Class implementation here
```

### 2. Create Logger
**Objective:** Implement `get_logger` function that returns a configured logger.
- **File:** `filtered_logger.py`
- **Function:** `get_logger()`

```python
def get_logger():
    # Function implementation here
```

### 3. Connect to Secure Database
**Objective:** Implement `get_db` function to connect to a secure database using environment variables.
- **File:** `filtered_logger.py`
- **Function:** `get_db()`

```python
def get_db():
    # Function implementation here
```

### 4. Read and Filter Data
**Objective:** Implement a `main` function to retrieve and display filtered user data.
- **File:** `filtered_logger.py`
- **Function:** `main()`

```python
def main():
    # Function implementation here
```

### 5. Encrypting Passwords
**Objective:** Implement `hash_password` function to encrypt passwords.
- **File:** `encrypt_password.py`
- **Function:** `hash_password(password)`

```python
def hash_password(password):
    # Function implementation here
```

### 6. Check Valid Password
**Objective:** Implement `is_valid` function to validate encrypted passwords.
- **File:** `encrypt_password.py`
- **Function:** `is_valid(hashed_password, password)`

```python
def is_valid(hashed_password, password):
    # Function implementation here
```

## Resources
- [What Is PII, non-PII, and Personal Data?](https://example.com)
- [logging documentation](https://docs.python.org/3/library/logging.html)
- [bcrypt package](https://pypi.org/project/bcrypt/)
- [Logging to Files, Setting Levels, and Formatting](https://docs.python.org/3/howto/logging.html)

## Repository Structure
```plaintext
alx-backend-user-data/
├── 0x00-personal_data/
│   ├── filtered_logger.py
│   └── encrypt_password.py
├── main.py
└── README.md
```

## How to Run
1. **Clone the repository:**
    ```sh
    git clone https://github.com/your-username/alx-backend-user-data.git
    cd alx-backend-user-data
    ```

2. **Set up the database:**
    ```sh
    cat main.sql | mysql -uroot -p
    ```

3. **Run the main program:**
    ```sh
    PERSONAL_DATA_DB_USERNAME=root PERSONAL_DATA_DB_PASSWORD=root PERSONAL_DATA_DB_HOST=localhost PERSONAL_DATA_DB_NAME=my_db ./main.py
    ```

## Author

- **@waltertaya**
