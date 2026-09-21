# CLI Student Expense Tracker

A lightweight, object-oriented Command-Line Interface (CLI) application designed to help students track their daily expenses locally without any overhead. This tool is built entirely with pure Python, utilizing CSV-based storage and native argument parsing.

---

## Features

- **Quick Add:** Record transactions instantly directly from your terminal, including amount, category, and notes.
- **Categorization:** Group expenses dynamically based on your needs (e.g., makanan, transport, kuliah, hiburan).
- **Expense Breakdown (Summary):** Aggregate total spending per category with automatic percentage calculations.
- **Record Management (Delete):** Remove specific entries effortlessly using unique transaction IDs.
- **Indonesian Rupiah Formatting:** View reports with standard Indonesian currency separators (`Rp25.000`).
- **Zero External Dependencies:** Built entirely using the Python standard library (`csv`, `argparse`, `datetime`), meaning no `pip install` required.

---

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Alif-fiansyah/cli-expense-tracker.git
   cd cli-expense-tracker
   ```

2. **Run the script (Requires Python 3.8+):**
   ```bash
   python tracker.py -h
   ```

---

## Usage Examples

### Adding an Expense
General Syntax:
```bash
python tracker.py add <amount> "<note>" -c <category>
```

Example:
```bash
python tracker.py add 25000 "Makan siang ayam geprek" -c makanan
python tracker.py add 15000 "Bensin motor" -c transport
python tracker.py add 12000 "Fotokopi materi kuliah" -c kuliah
```

### Viewing All Expenses
To inspect full transaction history along with unique IDs and totals:
```bash
python tracker.py list
```

### Expense Summary & Statistics
To view total spending grouped by category with percentages:
```bash
python tracker.py summary
```
### Deleting a Transaction
To remove an entry using its ID obtained from the list command:
```bash
python tracker.py delete <transaction_id>
```

### Sample Output

#### List View (`python tracker.py list`)
```text
================================================================================
ID           | Tanggal          | Kategori     |        Nominal | Catatan
--------------------------------------------------------------------------------
1726910400   | 2026-09-21 12:00 | Makanan      |       Rp25.000 | Makan siang ayam geprek
1726910415   | 2026-09-21 12:05 | Transport    |       Rp15.000 | Bensin motor
1726910430   | 2026-09-21 12:10 | Kuliah       |       Rp12.000 | Fotokopi materi kuliah
================================================================================
TOTAL PENGELUARAN: Rp52.000
```

### Category Summary  (`python tracker.py summary`)
```text
=============================================
Kategori           |          Total | Persentase
---------------------------------------------
Makanan            |       Rp25.000 |   48.1%
Transport          |       Rp15.000 |   28.8%
Kuliah             |       Rp12.000 |   23.1%
=============================================
TOTAL: Rp52.000
```


---

## Tech Stack & Architecture

- **Language:** Python 3
- **Design Pattern:** Object-Oriented Programming (OOP)
  - `Expense`: Data modeling for single transactions.
  - `ExpenseTracker`: Handles storage persistence and business logic.
- **Storage:** Local CSV File System
