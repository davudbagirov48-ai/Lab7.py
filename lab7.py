# ============================================
# ЛАБОРАТОРНАЯ №7 — Интерполяционный полином Ньютона
# Вариант 2
# Полный жирный код (максимальная версия)
# ============================================

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from math import factorial

# --------------------------------------------
# Исходные данные (вариант 2)
# --------------------------------------------
x = np.array([0.101, 0.106, 0.111, 0.116, 0.121,
              0.126, 0.131, 0.136, 0.141, 0.146, 0.151])

y = np.array([1.2618, 1.2764, 1.2912, 1.3061, 1.3213,
              1.3366, 1.3520, 1.3677, 1.3835, 1.3995, 1.4157])

# --------------------------------------------
# Функция построения таблицы конечных разностей
# --------------------------------------------
def finite_differences(y):
    table = [y]
    for i in range(1, len(y)):
        new_row = np.diff(table[i-1])
        table.append(new_row)
    return table

diff_table = finite_differences(y)

# --------------------------------------------
# Функция Ньютона (универсальная)
# --------------------------------------------
def newton_interp(X, x, diff_table):
    h = x[1] - x[0]
    x0 = x[0]
    q = (X - x0) / h

    result = diff_table[0][0]
    q_term = 1

    for i in range(1, len(diff_table)):
        q_term *= (q - (i - 1))
        result += diff_table[i][0] * q_term / factorial(i)

    return result

# --------------------------------------------
# Вычисления по варианту
# --------------------------------------------
x1 = 0.112
x2 = 0.145

f1 = newton_interp(x1, x, diff_table)
f2 = newton_interp(x2, x, diff_table)

print("=======================================")
print("   РЕЗУЛЬТАТЫ ВЫЧИСЛЕНИЙ (ВАРИАНТ 2)   ")
print("=======================================\n")

print(f"f(0.112) = {f1:.6f}")
print(f"f(0.145) = {f2:.6f}")

# --------------------------------------------
# Таблица конечных разностей в красивом виде
# --------------------------------------------
max_len = max(len(row) for row in diff_table)
padded = []

for row in diff_table:
    padded.append(list(row) + [None] * (max_len - len(row)))

df = pd.DataFrame(
    padded,
    index=[f"Δ^{i}y" for i in range(len(diff_table))]
).T

print("\n---------------------------------------")
print("     ТАБЛИЦА КОНЕЧНЫХ РАЗНОСТЕЙ")
print("---------------------------------------")
print(df)

# --------------------------------------------
# Построение графика интерполяции Ньютона
# --------------------------------------------
xx = np.linspace(min(x), max(x), 400)
yy = [newton_interp(xi, x, diff_table) for xi in xx]

plt.figure(figsize=(10, 6))
plt.plot(x, y, 'o', label='Исходные точки', markersize=8)
plt.plot(xx, yy, label='Интерполяционный полином Ньютона', linewidth=2)

plt.title("Интерполяция Ньютона — Вариант 2", fontsize=16)
plt.xlabel("x", fontsize=14)
plt.ylabel("y", fontsize=14)
plt.grid(True)
plt.legend(fontsize=12)
plt.show()

# --------------------------------------------
# Дополнительный график — разности
# --------------------------------------------
plt.figure(figsize=(10, 6))

for i in range(1, len(diff_table)):
    plt.plot(diff_table[i], label=f"Δ^{i}y")

plt.title("Графики конечных разностей", fontsize=16)
plt.xlabel("Элемент", fontsize=14)
plt.ylabel("Значение", fontsize=14)
plt.grid(True)
plt.legend(fontsize=12)
plt.show()

print("\nГотово! Все графики построены, таблицы выведены.")
