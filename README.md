# CLI Student Expense Tracker

A lightweight, object-oriented Command-Line Interface (CLI) application designed to help students track their daily expenses locally without any overhead. This tool is built entirely with pure Python, utilizing CSV-based storage and native argument parsing.

---

## Features

- **Quick Add**: Record transactions instantly directly from your terminal, including amount, category, and notes.
- **Categorization**: Group expenses dynamically based on your needs (e.g., makanan, transport, kuliah, hiburan).
- **Summary & Formatting**: View an auto-formatted ASCII table report complete with currency formatting and calculated totals.
- **Zero External Dependencies**: Built entirely using the Python standard library (csv, argparse, datetime), meaning no pip install required.

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
Syntax umum:
```bash
python tracker.py add <amount> "<note>" -c <category>
```

Contoh penambahan transaksi:
```bash
python tracker.py add 25000 "Makan siang ayam geprek" -c makanan
python tracker.py add 15000 "Bensin motor" -c transport
```

### Viewing All Expenses
Untuk melihat seluruh riwayat transaksi dan total pengeluaran:
```bash
python tracker.py list
```

### Sample Output
```text
=================================================================
Tanggal            | Kategori     | Nominal (Rp)    | Catatan
-----------------------------------------------------------------
2026-09-17 15:22   | Makanan      |       25,000    | Makan siang ayam geprek
2026-09-17 15:22   | Transport    |       15,000    | Bensin motor
=================================================================
TOTAL PENGELUARAN: Rp40,000
```

---

## Tech Stack & Architecture

- **Language:** Python 3
- **Design Pattern:** Object-Oriented Programming (OOP)
  - `Expense`: Data modeling for single transactions.
  - `ExpenseTracker`: Handles storage persistence and business logic.
- **Storage:** Local CSV File System
