# STORE-

## Overview

The Store is a Python-based application that allows users to create accounts, purchase products, and view their order history. It also provides an admin feature to manage and view all orders and users.

### User Features

- Register and log in securely using hashed passwords.
- Browse available Pokémon card products.
- Place orders and view order history.

### Admin Features

- View all users and their roles.
- Update user roles (e.g., promote to admin).
- Delete users.
- Add, update, and delete products.
- View all orders placed by users.

---

## Tech Stack

| **Category**    | **Tech**                                                          |
| --------------- | ----------------------------------------------------------------- |
| **Language**    | Python                                                            |
| **Backend**     | Core Python libraries (`pymongo`, `bcrypt`, `getpass`, `logging`) |
| **Database**    | MongoDB                                                           |
| **Development** | VS Code, Git, `venv`, `pip`                                       |
| **Utilities**   | `logging`, `datetime`                                             |

---

## Requirement

- python 3.10.6

```
pip install requirements.txt
```

## Project Structure

```
store-app
├── src
│   ├── __init__.py
│   ├── main.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── account.py
│   │   ├── product.py
│   │   └── order.py
│   ├── services
│   │   ├── __init__.py
│   │   ├── account_service.py
│   │   ├── product_service.py
│   │   └── order_service.py
│   ├── controllers
│   │   ├── __init__.py
│   │   ├── account_controller.py
│   │   ├── product_controller.py
│   │   └── order_controller.py
│   └── utils
│       ├── __init__.py
│       └── logger.py
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd store-app
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command:

```
python store.py
```
