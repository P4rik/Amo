
import tkinter as tk
import math
from tkinter import filedialog

root = tk.Tk()
root.title("Лабораторна робота №1")
root.configure(bg="lavender")

def read_values_from_file(entries):
    file_path = filedialog.askopenfilename(title="Оберіть файл", filetypes=[("Text files", "*.txt")])
    if file_path:
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                for entry, line in zip(entries, lines):
                    value = float(line.strip())
                    entry.delete(0, 'end')
                    entry.insert(0, value)
        except (ValueError, FileNotFoundError):
            print("Не вдалося зчитати дані з файлу!")

def open_window():
    window = tk.Tk()
    window.title("Лінійний алгоритм")
    window.configure(bg="lavender")
    label = tk.Label(window, text="Алгоритм: Y1=2*cos(b*c/2)+2*sin(c*b/2)",font=("Arial", 12),bg="lavender")
    label.pack()

    def calculate():
        try:
         values = [float(entry.get()) for entry in entries]
         b, c = values

         y1 = 2 * math.cos(b * c / 2) + 2 * math.sin(c * b / 2)

         result_label.config(text="Результат: Y1 = {:.2f}".format(y1),font=("Arial", 13),bg="lavender")
        except ValueError:
            result_label.config(text="Помилка!Будь ласка, введіть значення",font=("Arial", 12),bg="lavender")


    labels_text = ["Введіть b:","Введіть c:"]
    entries = []
    def set_font(label):
        label.config(font=("Arial", 12),bg="lavender")

    for text in labels_text:
        label = tk.Label(window, text=text)
        label.pack()
        entry = tk.Entry(window)
        entry.pack()
        entries.append(entry)
        set_font(label)

    def read_from_file():
        read_values_from_file(entries)

    read_button = tk.Button(window, text="Зчитати з файлу", command=read_from_file,font=("Arial", 12))
    read_button.pack()

    calculate_button = tk.Button(window, text="Обчислити", command=calculate,font=("Arial", 12))
    calculate_button.pack()

    result_label = tk.Label(window, text="",bg="lavender")
    result_label.pack()

    window.mainloop()


def open_window2():
    window2 = tk.Tk()
    window2.title("Алгоритм, що розгалужується")
    window2.configure(bg="lavender")
    label = tk.Label(window2, text="Алгоритм: y=sqrt((d-b-kj)/(23*sqrt(g*f)+6*sqrt(v*c)))", font=("Arial", 12),bg="lavender")
    label.pack()

    labels_text = ["Введіть d:", "Введіть b:", "Введіть k:", "Введіть j:", "Введіть g:", "Введіть f:", "Введіть v:","Введіть c:"]
    entries = []

    def set_font(label):
        label.config(font=("Arial", 12),bg="lavender")

    for text in labels_text:
        label = tk.Label(window2, text=text)
        label.pack()
        entry = tk.Entry(window2)
        entry.pack()
        entries.append(entry)
        set_font(label)

    def calculate1():
        try:
            values = [float(entry.get()) for entry in entries]
            d, b, k, j, g, f, v, c = values

            divisor = 23 * math.sqrt(g * f) + 6 * math.sqrt(v * c)

            if divisor == 0:
                result_label.config(text="Ділення на нуль. Будь ласка, введіть нові значення", font=("Arial", 12), bg="lavender")
            elif (d - b - k * j) < 0 or g * f < 0 or v * c < 0:
                result_label.config(text="Підкореневий вираз від'ємний. Будь ласка, введіть нові значення",font=("Arial", 12), bg="lavender")
            else:
                y = math.sqrt((d - b - k * j) / divisor)
                result_label.config(text="Результат: y = {:.2f}".format(y), font=("Arial", 13), bg="lavender")
        except ValueError:
            result_label.config(text="Помилка! Будь ласка, введіть числові значення", font=("Arial", 12), bg="lavender")
    def read_from_file():
        read_values_from_file(entries)
    read_button = tk.Button(window2, text="Зчитати з файлу", command=read_from_file, font=("Arial", 12))
    read_button.pack()

    calculate_button = tk.Button(window2, text="Обчислити", command=calculate1, font=("Arial", 12))
    calculate_button.pack()


    result_label = tk.Label(window2, text="",bg="lavender")
    result_label.pack()

    window2.mainloop()

def open_window3():
    window3 = tk.Tk()
    window3.title("Циклічний алгоритм")
    window3.configure(bg="lavender")
    label = tk.Label(window3, text="Алгоритм: f=SUM[0<i<50](a^2+56*c*sqrt(k*g))",font=("Arial", 12),bg="lavender")
    label.pack()
    labels_text = ["Введіть a:", "Введіть c:", "Введіть k:", "Введіть g:"]
    entries = []

    def set_font(label):
        label.config(font=("Arial", 12),bg="lavender")

    for text in labels_text:
        label = tk.Label(window3, text=text)
        label.pack()
        entry = tk.Entry(window3)
        entry.pack()
        entries.append(entry)
        set_font(label)
    def calculate2():
        try:
            values = [float(entry.get()) for entry in entries]
            a, c, k, g = values
            f = 0


            if k * g < 0:
                result_label.config(text="Підкореневий вираз від'ємний. Будь ласка, введіть нові значення",font=("Arial", 13), bg="lavender")
            else:
                for i in range(1, 50):
                    f += (a ** 2 + 56 * c * math.sqrt(k * g))
                result_label.config(text="Результат: f = {:.2f}".format(f),font=("Arial", 13), bg="lavender")
        except ValueError:
            result_label.config(text="Помилка! Будь ласка, введіть нові значення", font=("Arial", 12),bg="lavender")


    def read_from_file():
        read_values_from_file(entries)

    read_button = tk.Button(window3, text="Зчитати з файлу", command=read_from_file,font=("Arial", 12))
    read_button.pack()

    calculate_button = tk.Button(window3, text="Обчислити", command=calculate2,font=("Arial", 12))
    calculate_button.pack()

    result_label = tk.Label(window3, text="",bg="lavender")
    result_label.pack()

    window3.mainloop()


button = tk.Button(root, text="Лійнійний алгоритм", command=open_window,font=("Arial", 12))
button.pack()
button2 = tk.Button(root, text="Алгоритм, що розгалужується", command=open_window2,font=("Arial", 12))
button2.pack()
button3 = tk.Button(root, text="Циклічний алгоритм", command=open_window3,font=("Arial", 12))
button3.pack()

label = tk.Label(root, text="Залевська Олена Олегівна",font=("Arial", 12),pady=10,bg="lavender")
label.pack()
label2 = tk.Label(root, text="Група: ІО-24",font=("Arial", 12),bg="lavender")
label2.pack()
label3 = tk.Label(root, text="Варіант: 12",font=("Arial", 12),bg="lavender")
label3.pack()

root.mainloop()
