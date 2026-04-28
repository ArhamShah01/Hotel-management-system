# Hotel Management System

A Python-based hotel management system with MySQL database integration for managing customer reservations, room bookings, and billing.

## Features

- Customer management (add, search, update, delete)
- Room inventory tracking with 5 room types
- Check-in/check-out management
- Billing system (room rent, food, games, transport)
- Loyalty program with unique membership IDs
- CSV data import/export

## Installation

```bash
pip install mysql-connector-python pandas
```

## Setup

1. Create MySQL database:
```sql
CREATE DATABASE HOTEL_MANAGEMENT;
```

2. Update database credentials in `main.py`:
```python
db = mysql.connector.connect(
    host='localhost',
    user='your_username',
    password='your_password',
    database='HOTEL_MANAGEMENT'
)
```

3. Prepare `customer_data.csv` with customer records

## Usage

Run the script:
```bash
python main.py
```

### Available Functions

- `display()` - View all customer records
- `search()` - Search customer by code
- `update()` - Update customer information
- `delete()` - Delete customer record
- `get_empty_rooms()` - Check room availability
- `print_random_letters_numbers()` - Generate loyalty ID

## Database Tables

- **Customer** - Customer information and check-in/out details
- **Room** - Room types, charges, and features
- **hoteldata** - Billing information

## Requirements

- Python 3.x
- MySQL Server
- Pandas

## License

Academic project - VIT Vellore
