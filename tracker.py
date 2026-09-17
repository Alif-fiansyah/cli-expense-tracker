import argparse
import csv
from datetime import datetime
import os

CSV_FILE = "expenses.csv"


class Expense:

  def __init__(self, amount, category, note, date=None, expense_id=None):
    self.id = expense_id or int(datetime.now().timestamp())
    self.amount = float(amount)
    self.category = category.lower()
    self.note = note
    self.date = date or datetime.now().strftime("%Y-%m-%d %H:%M")

  def to_list(self):
    """Mengubah objek menjadi list untuk disimpan di CSV."""
    return [self.id, self.amount, self.category, self.note, self.date]


class ExpenseTracker:

  def __init__(self, filepath=CSV_FILE):
    self.filepath = filepath
    self._init_storage()

  def _init_storage(self):
    """Buat file CSV beserta headernya jika file belum ada."""
    if not os.path.exists(self.filepath):
      with open(self.filepath, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Nominal", "Kategori", "Catatan", "Tanggal"])

  def add_expense(self, amount, category, note):
    expense = Expense(amount, category, note)
    with open(self.filepath, mode="a", newline="", encoding="utf-8") as file:
      writer = csv.writer(file)
      writer.writerow(expense.to_list())
    print(f"[OK] Berhasil mencatat Rp{expense.amount:,.0f} ({expense.category})")

  def list_expenses(self):
    if not os.path.exists(self.filepath):
      print("Belum ada data pengeluaran.")
      return

    total = 0.0
    print("\n" + "=" * 65)
    print(
        f"{'Tanggal':<18} | {'Kategori':<12} | {'Nominal (Rp)':<15} |"
        " {'Catatan'}"
    )
    print("-" * 65)

    with open(self.filepath, mode="r", encoding="utf-8") as file:
      reader = csv.DictReader(file)
      for row in reader:
        nominal = float(row["Nominal"])
        total += nominal
        print(
            f"{row['Tanggal']:<18} | {row['Kategori'].capitalize():<12} |"
            f" {nominal:>12,.0f}    | {row['Catatan']}"
        )

    print("=" * 65)
    print(f"TOTAL PENGELUARAN: Rp{total:,.0f}\n")


def main():
  parser = argparse.ArgumentParser(
      description="CLI Student Expense Tracker - Catat pengeluaran cepat via terminal"
  )
  subparsers = parser.add_subparsers(dest="command", help="Perintah yang tersedia")

  # Sub-command: add
  add_parser = subparsers.add_parser("add", help="Tambah pengeluaran baru")
  add_parser.add_argument("amount", type=float, help="Nominal uang (contoh: 20000)")
  add_parser.add_argument("note", type=str, help="Catatan pengeluaran (contoh: 'Nasi Padang')")
  add_parser.add_argument(
      "--category",
      "-c",
      type=str,
      default="lain-lain",
      help="Kategori (makanan, transport, kuliah, dll.)",
  )

  # Sub-command: list
  subparsers.add_parser("list", help="Lihat semua riwayat dan total pengeluaran")

  args = parser.parse_args()
  tracker = ExpenseTracker()

  if args.command == "add":
    tracker.add_expense(args.amount, args.category, args.note)
  elif args.command == "list":
    tracker.list_expenses()
  else:
    parser.print_help()


if __name__ == "__main__":
  main()