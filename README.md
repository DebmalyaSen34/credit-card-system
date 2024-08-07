# Credit Card Management System

## Introduction

Welcome to the Credit Card Management System! This application is designed to manage credit card information, user data, and transaction limits. It is built using Python and MySQL, providing a robust backend for secure and efficient data handling.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Database Schema](#database-schema)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Features

- Secure storage and management of credit card information
- User authentication and authorization
- Transaction processing and limit management
- Detailed logging and error handling

## Technologies Used

- **Backend:**
  - Python
  - Flask (or Django, if applicable)
  - RESTful API

- **Database:**
  - MySQL

## Database Schema

The database consists of several tables to handle users, credit cards, branches, limits, and applications. Below is the schema definition:

### Branch Table

\```sql
CREATE TABLE BRANCH(
  branch_id INT(10) NOT NULL,
  branch_name CHAR(20) NOT NULL,
  branch_address CHAR(25) NOT NULL,
  branch_manager CHAR(25) NOT NULL,
  CONSTRAINT pk_branch PRIMARY KEY (branch_id)
);
```

### User Table

\```sql
CREATE TABLE USER1 (
  user_id INT(20) NOT NULL,
  user_name CHAR(25) NOT NULL,
  user_mob VARCHAR(15) NOT NULL,
  user_mail VARCHAR(30) NOT NULL,
  user_address VARCHAR(50) NOT NULL,
  user_branch_id INT(10) NOT NULL,
  CONSTRAINT pk_user PRIMARY KEY (user_id),
  CONSTRAINT fk_user_branch FOREIGN KEY (user_branch_id) 
    REFERENCES BRANCH(branch_id) 
    ON DELETE CASCADE 
    ON UPDATE CASCADE
);
```

### Credit Card Table

\```sql
CREATE TABLE CREDIT_CARD(
  crc_name VARCHAR(25) NOT NULL,
  crc_id INT(15) NOT NULL,
  crc_bal INT(10) NOT NULL,
  crc_type VARCHAR(15) NOT NULL,
  crc_user_id INT(20) NOT NULL,
  CONSTRAINT pk_credit_card PRIMARY KEY (crc_id),
  CONSTRAINT p_crc_id FOREIGN KEY (crc_user_id) 
    REFERENCES USER1(user_id) 
    ON DELETE CASCADE 
    ON UPDATE CASCADE
);
```

### Limits Table

\```sql
CREATE TABLE LIMITS(
  limit_user_id INT(15) NOT NULL,
  limit_bal INT(10) NOT NULL,
  limit_crc_id INT(15) NOT NULL,
  CONSTRAINT pk_limits PRIMARY KEY (limit_user_id),
  CONSTRAINT p_limit_id FOREIGN KEY (limit_crc_id) 
    REFERENCES CREDIT_CARD(crc_id) 
    ON DELETE CASCADE 
    ON UPDATE CASCADE
);
```

### Applications Table

\```sql
CREATE TABLE APPLICATIONS(
  app_num INT(10) NOT NULL,
  app_user_id INT(20) NOT NULL,
  app_type VARCHAR(20) NOT NULL,
  CONSTRAINT pk_applications PRIMARY KEY (app_num),
  CONSTRAINT p_app_id FOREIGN KEY (app_user_id)
    REFERENCES USER1(user_id) 
    ON DELETE CASCADE 
    ON UPDATE CASCADE
);
\```

## Installation

### Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- MySQL

### Backend Setup

1. Clone the repository:

   \```bash
   git clone https://github.com/yourusername/credit_card_management_system.git
   cd credit_card_management_system
   \```

2. Create a virtual environment and activate it:

   \```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   \```

3. Install the required Python packages:

   \```bash
   pip install -r requirements.txt
   \```

4. Set up the MySQL database:

   \```sql
   CREATE DATABASE credit_card_system;
   \```

5. Update the database configuration in `config.py`:

   \```python
   SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@localhost/credit_card_system'
   \```

6. Initialize the database:

   \```bash
   flask db init
   flask db migrate
   flask db upgrade
   \```

7. Run the backend server:

   \```bash
   flask run
   \```

## Usage

1. Access the application via the provided API endpoints.
2. Use a tool like Postman or cURL to interact with the API.
3. Register a new user account or log in with an existing account.
4. Add, validate, and manage credit card information.
5. Process transactions securely.

## API Endpoints

### User Authentication

- **POST /api/register**
  - Registers a new user.
  - Request body: `{ "username": "example", "password": "password" }`

- **POST /api/login**
  - Authenticates a user.
  - Request body: `{ "username": "example", "password": "password" }`

### Credit Card Management

- **POST /api/credit-cards**
  - Adds a new credit card.
  - Request body: `{ "card_number": "1234 5678 9012 3456", "expiry_date": "12/24", "cvv": "123" }`

- **GET /api/credit-cards**
  - Retrieves all credit cards for the authenticated user.

- **DELETE /api/credit-cards/{id}**
  - Deletes a credit card by ID.

### Transaction Management

- **POST /api/transactions**
  - Creates a new transaction.
  - Request body: `{ "amount": 100.00, "merchant": "Example Store", "credit_card_id": 1 }`

- **GET /api/transactions**
  - Retrieves all transactions for the authenticated user.

## Contributing

We welcome contributions from the community! To contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Make your changes and commit them: `git commit -m 'Add new feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Submit a pull request.