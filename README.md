# Hotel Management System

A terminal-based hotel management system built with Python and MySQL. Handles end-to-end guest operations — from check-in to billing — for a fictional five-star property, the Taj Mahal Palace, Mumbai.

---

## Features

- **Room Booking** — 5 room categories across 2,500 rooms with live availability tracking
- **Guest Management** — Add, search, update, and delete customer records
- **Automated Billing** — Room rent, food, amenities, and airport transfers consolidated into a final bill with 5% tax
- **Loyalty Program** — Membership enrollment with generated IDs and 10% discount on room rent *(see Known Limitations)*
- **CSV Import/Export** — Bulk-load guest records from CSV on startup; new bookings are mirrored to a CSV backup
- **Input Validation** — Date format enforcement, type checks, and duplicate-safe imports

---

## Room Types

| Range | Type | Rate/Night | Max Occupancy |
|---|---|---|---|
| 1 – 500 | Duplex | ₹15,000 | 5 |
| 501 – 1000 | Cabana | ₹12,500 | 3 |
| 1001 – 1500 | Lanai | ₹20,000 | 4 |
| 1501 – 2000 | Suite | ₹25,000 | 12 |
| 2001 – 2500 | Mini | ₹7,500 | 2 |

---

## Prerequisites

- Python 3.8+
- MySQL Server 8.0+
- pip packages: `mysql-connector-python`, `pandas`

```bash
pip install mysql-connector-python pandas
```

---

## Setup

**1. Create the database**

```sql
CREATE DATABASE HOTEL_MANAGEMENT;
```

**2. Configure credentials**

Set your MySQL password as an environment variable (the script reads it via `os.getenv`):

```bash
# Linux / macOS
export SQL_PASSWORD=your_password

# Windows (Command Prompt)
set SQL_PASSWORD=your_password
```

Alternatively, edit the connection block in `main.py` directly:

```python
db = mysql.connector.connect(
    host='localhost',
    user='your_username',
    password='your_password',
    database='HOTEL_MANAGEMENT'
)
```

**3. (Optional) Seed guest data**

Place a `customer_data.csv` file in the project root. The script imports it automatically on startup, skipping malformed rows. Expected column order:

```
CustomerCode, Name, IDType, IDNumber, Address, Nationality,
CheckInDate (DD-MM-YYYY), CheckOutDate (DD-MM-YYYY), RoomNo,
ContactNumber, Purpose (B/L), Smoking (Yes/No), Menu, Airport, Loyalty
```

---

## Running

```bash
python main.py
```

---

## Usage

The system presents a simple numbered menu at every level — no GUI required.

```
Main Menu
  1. Hotel Speciality     → View room descriptions and hotel amenities
  2. Customer Management  → Access all booking and record operations
  3. Exit

Customer Management
  1. Book a Room
  2. Show All Customer Records
  3. Search Customer Record
  4. Delete Customer Record
  5. Update Customer Record
  6. Return to Main Menu
```

### Booking a Room

The booking flow collects:
- Guest details (name, ID, address, nationality, contact)
- Check-in and check-out dates
- Room preference (from live availability)
- Smoking preference
- Restaurant meal plan (optional)
- Airport pickup/drop (optional)
- Amenity hours — table tennis, bowling, snooker, video games, pool, conference hall
- Loyalty membership status

A final itemised bill is printed and the record is saved to both MySQL and the CSV backup.

---

## Database Schema

### `Customer`
Stores guest profile and stay details (check-in/out dates, room number, preferences).

### `hoteldata`
Stores the billing breakdown per booking (room rent, food, games, transport, totals).

### `Room`
Static reference table seeded once with the five room types, their charges, features, and occupancy limits.

---

## Known Limitations

### ⚠️ Loyalty Program — Not Validated

The loyalty membership check currently **accepts any code the guest provides without verification**. There is no lookup against a membership database. This means:

- A guest claiming to be a member receives the 10% discount unconditionally.
- Newly enrolled members receive a randomly generated ID, but it is not persisted anywhere — so it cannot be verified on a return visit.

**This is a placeholder implementation.** A future version should maintain a `LoyaltyMembers` table, validate codes against it on check-in, and write new enrolments to it at registration.

---

## Project Structure

```
├── main.py               # All application logic
├── customer_data.csv     # Seed data (imported on startup)
├── customer_data_v3.csv  # Backup written by the application (auto-created)
└── README.md
```

---

## License

MIT — see [LICENSE](LICENSE) for details.

---

## Academic Note

This project was developed as part of an academic submission at VIT Vellore.