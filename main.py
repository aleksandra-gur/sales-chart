import matplotlib.pyplot as plt

months = ["Янв", "Фев", "Мар", "Апр", "Май", "Июн"]
sales = [120, 145, 180, 165, 210, 235]

plt.plot(months, sales)
plt.title("Продажи по месяцам")
plt.xlabel("Месяц")
plt.ylabel("Сумма, тыс. руб.")
plt.show()
