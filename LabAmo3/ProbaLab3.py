from tkinter import *
from tkinter import ttk
import numpy as np
import math
import matplotlib.pyplot as plt

# Функція для інтерполяції методом Лагранжа
def lagrange_interpolation(nodes, x_values, y_values):
    n = len(nodes)
    result = 0.0
    for i in range(n):
        term = y_values[i]
        for j in range(n):
            if j != i:
                term *= (x_values - nodes[j]) / (nodes[i] - nodes[j])
        result += term
    return result

# Задана функція
def f(x):
    return x**2 + 2 * math.exp(x)

# Обчислення похибки
def compute_error(true_value, interpolated_value):
    return abs(true_value - interpolated_value)

# Функція для заповнення таблиці
def fill_table():
    a = float(entry_a.get())
    b = float(entry_b.get())
    n = int(entry_n.get())
    x = float(entry_x.get())

    nodes = generate_nodes(a, b, n)
    true_values = [f(node) for node in nodes]
    interpolated_value = lagrange_interpolation(nodes, x, true_values)
    true_value = f(x)
    error = compute_error(true_value, interpolated_value)
    difference = true_value - interpolated_value
    refinement_coefficient = 1 - difference / error if error != 0 else 0

    tree.insert("", "end", text=f"x = {x}", values=(error, difference, refinement_coefficient))

# Функція для інтерполяції та побудови графіку
def interpolate_and_plot():
    a = float(entry_a.get())
    b = float(entry_b.get())
    n = int(entry_n.get())

    nodes = generate_nodes(a, b, n)
    x_values = np.linspace(a, b, 100)
    y_values = [f(x) for x in x_values]

    true_values = [f(node) for node in nodes]
    interpolated_values = [lagrange_interpolation(nodes, x, true_values) for x in x_values]
    errors = [compute_error(true_val, interp_val) for true_val, interp_val in zip(y_values, interpolated_values)]

    plt.plot(x_values, y_values, label="Справжня Функція")
    plt.plot(x_values, interpolated_values, label="Інтерполяція")
    plt.scatter(nodes, true_values, color='red', label="Вузли Інтерполяції")
    plt.legend()
    plt.show()

    # Виведення значень похибки
    print("Максимальна Похибка:", max(errors))
    print("Середня Похибка:", np.mean(errors))
    print("Стандартне Відхилення Похибки:", np.std(errors))

# Функція для генерації вузлів інтерполяції
def generate_nodes(a, b, n):
    h = (b - a) / n
    return [a + i * h for i in range(n + 1)]

# Головна функція
def main():
    global entry_a, entry_b, entry_n, entry_x, tree

    root = Tk()
    root.title("Інтерполяція методом Лагранжа")

    frame = Frame(root)
    frame.pack(padx=10, pady=10)

    label_a = Label(frame, text="a:")
    label_a.grid(row=0, column=0)
    entry_a = Entry(frame)
    entry_a.grid(row=0, column=1)
    entry_a.insert(END, "0")

    label_b = Label(frame, text="b:")
    label_b.grid(row=1, column=0)
    entry_b = Entry(frame)
    entry_b.grid(row=1, column=1)
    entry_b.insert(END, "1")

    label_n = Label(frame, text="n:")
    label_n.grid(row=2, column=0)
    entry_n = Entry(frame)
    entry_n.grid(row=2, column=1)
    entry_n.insert(END, "10")

    label_x = Label(frame, text="x:")
    label_x.grid(row=3, column=0)
    entry_x = Entry(frame)
    entry_x.grid(row=3, column=1)
    entry_x.insert(END, "0.5")

    button_fill_table = Button(frame, text="Заповнити Таблицю", command=fill_table)
    button_fill_table.grid(row=4, columnspan=2)

    tree = ttk.Treeview(root)
    tree["columns"] = ("error", "difference", "refinement_coefficient")
    tree.heading("error", text="Похибка")
    tree.heading("difference", text="Різниця")
    tree.heading("refinement_coefficient", text="Коефіцієнт Уточнення")
    tree.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
