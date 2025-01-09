# STORE-APP

## Overview
The Store App is a Python-based application that allows users to create accounts, purchase products, and view their order history. It also provides an admin feature to manage and view all orders and users.

## Features
- User account creation and management
- Product browsing and purchasing
- Order history tracking
- Admin dashboard for managing users and orders

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
python src/main.py
```

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License.