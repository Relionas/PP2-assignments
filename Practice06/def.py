import os
from functools import reduce
if not os.path.exists("sales"):
    os.makedirs("sales")
    with open("sales/store1.txt", "w") as f:
        f.write("Laptop,3\nMouse,10\nKeyboard,5\nMonitor,2\nHeadphones,4")
    with open("sales/store2.txt", "w") as f:
        f.write("Laptop,7\nMouse,12\nKeyboard,8\nMonitor,1\nHeadphones,6")
    with open("sales/store3.txt", "w") as f:
        f.write("Laptop,4\nMouse,15\nKeyboard,3\nMonitor,5\nHeadphones,9")
    print("Создано")
products = []
files = os.listdir("sales")
for file_name in files:
    if file_name.endswith('.txt'):
        path = os.path.join("sales", file_name)
        with open(path, "r") as f:
            for line in f:
                if line.strip():
                    name, qty = line.strip().split(",")
                    products.append((name, int(qty)))

print(f"Найдено записей: {len(products)}")
total_records = len(products)
total_qty = sum(p[1] for p in products)
highest_sale = max(products, key=lambda x: x[1])
lowest_sale = min(products, key=lambda x: x[1])
boosted = list(map(lambda x: (x[0], x[1] + 2), products))
popular = list(filter(lambda x: x[1] > 5, products))
all_qtys = [p[1] for p in products]
product_of_all = reduce(lambda x, y: x * y, all_qtys)
print("\n Список товаров с индексами:")
for i, (name, qty) in enumerate(products, 1):
    print(f"{i}. {name}: {qty} шт.")
names = [p[0] for p in products]
qtys = [p[1] for p in products]
zipped = list(zip(names, qtys))
print(f"\nПример zip(): первые 3 -> {zipped[:3]}")
sorted_list = sorted(products, key=lambda x: x[1], reverse=True)
with open("sales_report.txt", "w", encoding='utf-8') as report:
    report.write("=" * 40 + "\n")
    report.write("ОТЧЕТ О ПРОДАЖАХ\n")
    report.write("=" * 40 + "\n\n")
    
    report.write(f"Всего записей: {total_records}\n")
    report.write(f"Общее количество: {total_qty}\n")
    report.write(f"Среднее количество: {total_qty / total_records:.1f}\n")
    report.write(f"Максимум: {highest_sale[1]} ({highest_sale[0]})\n")
    report.write(f"Минимум: {lowest_sale[1]} ({lowest_sale[0]})\n\n")
    
    report.write("ПОПУЛЯРНЫЕ ТОВАРЫ (>5 шт.):\n")
    if popular:
        for name, qty in popular:
            report.write(f"  {name}: {qty} шт.\n")
    else:
        report.write("  Нет товаров с продажами >5\n")
    
    report.write("\n" + "=" * 40 + "\n")
    report.write("ДОПОЛНИТЕЛЬНАЯ ИНФОРМАЦИЯ\n")
    report.write("=" * 40 + "\n\n")
    report.write(f"Произведение всех количеств: {product_of_all:,}\n\n")
    
    report.write("ТОВАРЫ ПО УБЫВАНИЮ:\n")
    for name, qty in sorted_list[:5]:
        report.write(f"  {name}: {qty} шт.\n")
print("Отчет сохранен в 'sales_report.txt'.")