import matplotlib.pyplot as plt

months = ["Янв", "Фев", "Мар", "Апр", "Май", "Июн"]
sales = [120, 145, 180, 165, 210, 235]

plt.plot(months, sales)
plt.title("Продажи по месяцам")
plt.xlabel("Месяц")
plt.ylabel("Сумма, тыс. руб.")
plt.show()

import csv
import matplotlib.pyplot as plt

def load_sales(path):
    months, sales = [], []
    with open(path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            months.append(row["month"])
            sales.append(int(row["sales"]))
    return months, sales

def main():
    months, sales = load_sales("data/sales.csv")
    plt.plot(months, sales, marker="o")
    plt.title("Продажи по месяцам")
    plt.xlabel("Месяц")
    plt.ylabel("Сумма, тыс. руб.")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()

import argparse
import csv
import matplotlib.pyplot as plt

def load_sales(path):
    months, sales = [], []
    with open(path, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            months.append(row["month"])
            sales.append(int(row["sales"]))
    return months, sales

def plot(months, sales, kind, output):
    if kind == "bar":
        plt.bar(months, sales, color="#3498db")
    else:
        plt.plot(months, sales, marker="o", color="#3498db")
    plt.title("Продажи по месяцам")
    plt.xlabel("Месяц")
    plt.ylabel("Сумма, тыс. руб.")
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    if output:
        plt.savefig(output, dpi=150)
        print(f"График сохранён: {output}")
    else:
        plt.show()

def main():
    parser = argparse.ArgumentParser(description="График продаж")
    parser.add_argument("--data", default="data/sales.csv", help="путь к CSV")
    parser.add_argument("--kind", choices=["line", "bar"], default="line")
    parser.add_argument("--output", help="сохранить в файл вместо показа")
    args = parser.parse_args()

    months, sales = load_sales(args.data)
    plot(months, sales, args.kind, args.output)

if __name__ == "__main__":
    main()
    