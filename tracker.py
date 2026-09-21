import argparse
import csv
from datetime import datetime
import os

CSV_FILE = "expenses.csv"


def rupiah(val):
  return f"Rp{int(val):,}".replace(",", ".")


class Expense:

  def __init__(self, amount, category, note, date=None, expense_id=None):
    self.id = expense_id or int(datetime.now().timestamp())
    self.amount = float(amount)
    self.category = category.lower()
    self.note = note
    self.date = date or datetime.now().strftime("%Y-%m-%d %H:%M")

  def to_list(self):
    return [self.id, self.amount, self.category, self.note, self.date]


class ExpenseTracker:

  def __init__(self, filepath=CSV_FILE):
    self.filepath = filepath
    self._init_storage()

  def _init_storage(self):
    if not os.path.exists(self.filepath):
      with open(self.filepath, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Nominal", "Kategori", "Catatan", "Tanggal"])

  def add_expense(self, amount, category, note):
    expense = Expense(amount, category, note)
    with open(self.filepath, mode="a", newline="", encoding="utf-8") as file:
      writer = csv.writer(file)
      writer.writerow(expense.to_list())
    print(f"[OK] Berhasil mencatat {rupiah(expense.amount)} ({expense.category})")

  def list_expenses(self):
    if not os.path.exists(self.filepath):
      print("Belum ada data pengeluaran.")
      return

    total = 0.0
    print("\n" + "=" * 80)
    print(
        f"{'ID':<12} | {'Tanggal':<16} | {'Kategori':<12} |"
        f" {'Nominal':<14} | {'Catatan'}"
    )
    print("-" * 80)

    with open(self.filepath, mode="r", encoding="utf-8") as file:
      reader = csv.DictReader(file)
      rows = list(reader)
      if not rows:
        print("Belum ada transaksi tersimpan.")
        return

      for row in rows:
        nominal = float(row["Nominal"])
        total += nominal
        print(
            f"{row['ID']:<12} | {row['Tanggal']:<16} |"
            f" {row['Kategori'].capitalize():<12} | {rupiah(nominal):>12} |"
            f" {row['Catatan']}"
        )

    print("=" * 80)
    print(f"TOTAL PENGELUARAN: {rupiah(total)}\n")

  def delete_expense(self, expense_id):
    if not os.path.exists(self.filepath):
      print("File data tidak ditemukan.")
      return

    deleted = False
    rows = []
    with open(self.filepath, mode="r", encoding="utf-8") as file:
      reader = csv.DictReader(file)
      for row in reader:
        if row["ID"] == str(expense_id):
          deleted = True
          continue
        rows.append(row)

    if deleted:
      with open(self.filepath, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["ID", "Nominal", "Kategori", "Catatan", "Tanggal"],
        )
        writer.writeheader()
        writer.writerows(rows)
      print(f"[OK] Transaksi dengan ID {expense_id} berhasil dihapus.")
    else:
      print(f"[!] ID {expense_id} tidak ditemukan.")

  def show_summary(self):
    if not os.path.exists(self.filepath):
      print("Belum ada data.")
      return

    category_totals = {}
    grand_total = 0.0

    with open(self.filepath, mode="r", encoding="utf-8") as file:
      reader = csv.DictReader(file)
      for row in reader:
        nom = float(row["Nominal"])
        kat = row["Kategori"].capitalize()
        category_totals[kat] = category_totals.get(kat, 0.0) + nom
        grand_total += nom

    if grand_total == 0:
      print("Belum ada pengeluaran.")
      return

    print("\n" + "=" * 45)
    print(f"{'Kategori':<18} | {'Total':<14} | Persentase")
    print("-" * 45)
    for kat, total in sorted(
        category_totals.items(), key=lambda x: x[1], reverse=True
    ):
      percent = (total / grand_total) * 100
      print(f"{kat:<18} | {rupiah(total):>12} | {percent:>6.1f}%")
    print("=" * 45)
    print(f"TOTAL: {rupiah(grand_total)}\n")


def main():
  parser = argparse.ArgumentParser(
      description=(
          "CLI Student Expense Tracker - Catat pengeluaran cepat via terminal"
      )
  )
  subparsers = parser.add_subparsers(
      dest="command", help="Perintah yang tersedia"
  )

  # Sub-command: add
  add_parser = subparsers.add_parser("add", help="Tambah pengeluaran baru")
  add_parser.add_argument(
      "amount", type=float, help="Nominal uang (contoh: 20000)"
  )
  add_parser.add_argument(
      "note", type=str, help="Catatan pengeluaran (contoh: 'Nasi Padang')"
  )
  add_parser.add_argument(
      "--category",
      "-c",
      type=str,
      default="lain-lain",
      help="Kategori (makanan, transport, kuliah, dll.)",
  )

  # Sub-command: list
  subparsers.add_parser(
      "list", help="Lihat semua riwayat dan total pengeluaran"
  )

  # Sub-command: delete
  del_parser = subparsers.add_parser(
      "delete", help="Hapus transaksi berdasarkan ID"
  )
  del_parser.add_argument("id", type=str, help="ID transaksi yang akan dihapus")

  # Sub-command: summary
  subparsers.add_parser(
      "summary", help="Ringkasan pengeluaran per kategori & persentase"
  )

  args = parser.parse_args()
  tracker = ExpenseTracker()

  if args.command == "add":
    tracker.add_expense(args.amount, args.category, args.note)
  elif args.command == "list":
    tracker.list_expenses()
  elif args.command == "delete":
    tracker.delete_expense(args.id)
  elif args.command == "summary":
    tracker.show_summary()
  else:
    parser.print_help()


if __name__ == "__main__":
  main()