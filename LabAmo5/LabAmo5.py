import os.path
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog, messagebox

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def select_method():
    method = var.get()
    if method == 1:
        # Labels
        labelfr1.grid(row=0, column=2, columnspan=7, padx=(10, 10), sticky="snew")
        label_photo.grid(row=1, rowspan=6, column=2, columnspan=7, padx=(10, 10))
    else:
        labelfr1.grid_forget()
        label_photo.grid_forget()
    if method == 2:
        # Labels
        labelfr2.grid(row=0, column=2, columnspan=4, padx=(10, 10), sticky="snew")
        result_text.grid(row=5, column=2, columnspan=4, padx=(10, 10))
        # Entry
        matrix1.grid(row=1, column=2, padx=(10, 0))
        matrix2.grid(row=1, column=3)
        matrix3.grid(row=1, column=4)
        matrix4.grid(row=1, column=5, padx=(0, 10))

        matrix5.grid(row=2, column=2, padx=(10, 0))
        matrix6.grid(row=2, column=3)
        matrix7.grid(row=2, column=4)
        matrix8.grid(row=2, column=5, padx=(0, 10))

        matrix9.grid(row=3, column=2, padx=(10, 0))
        matrix10.grid(row=3, column=3)
        matrix11.grid(row=3, column=4)
        matrix12.grid(row=3, column=5, padx=(0, 10))
        # Button
        open_button.grid(row=4, column=2, columnspan=2, padx=(15,0), pady=15, sticky="snew")
        solve_button.grid(row=4, column=4, columnspan=2, padx=(0, 15), pady=15, sticky="snew")
    else:
        labelfr2.grid_forget()
        result_text.grid_forget()
        open_button.grid_forget()
        solve_button.grid_forget()
        matrix1.grid_forget()
        matrix2.grid_forget()
        matrix3.grid_forget()
        matrix4.grid_forget()
        matrix5.grid_forget()
        matrix6.grid_forget()
        matrix7.grid_forget()
        matrix8.grid_forget()
        matrix9.grid_forget()
        matrix10.grid_forget()
        matrix11.grid_forget()
        matrix12.grid_forget()


# Win 1
win = tk.Tk()
photo = tk.PhotoImage(file=(resource_path('icon.png')))
win.iconphoto(False, photo)
win.title("Вікно 1")
win.config(bg='#363636')
win.geometry("")
win.resizable(False, False)

G = 24
N = 20

# frame
panel = tk.Frame(win, bg='#252425', relief=tk.RAISED, bd=5).grid(row=0, rowspan=11, column=0, sticky='snew')
panel2 = tk.Frame(win, bg='#252425', relief=tk.RAISED, bd=5).grid(row=0, rowspan=11, columnspan=9, column=1,
                                                                  sticky='snew')
panel3 = tk.Frame(win, bg='#252425', relief=tk.RAISED, bd=5).grid(row=0, rowspan=11, column=1, columnspan=9, sticky='snew')
panel4 = tk.Frame(win, bg='#252425', relief=tk.RAISED, bd=5).grid(row=0, rowspan=11, column=1, sticky='snew')

# Label
labelname = tk.Label(panel, text=f'Паровенко Данило Едуардович\nМоя група: ІО-{G}\nМій варіант: {N}',
                     bg='#252425', fg='white',
                     font=('Calibri', 20, 'bold')).grid(row=7, column=0, padx=(20, 20), pady=(0, 20))

label_1 = tk.Label(panel, text='Панель керування:', font=('Calibri', 25, 'bold'), bg='#252425', fg='white',
                   height=0).grid(row=0, column=0, padx=(10, 10), pady=(30, 30))

# Radbut
var = tk.IntVar()
radb1 = tk.Radiobutton(panel, text='Завдання', variable=var, value=1, font=('Calibri', 25, 'bold'), bg='#977AF9',
                       fg='black', state=tk.NORMAL, width=22, activebackground='#760598', relief=tk.RAISED,
                       bd='5', command=select_method).grid(row=4, column=0, pady=(10, 10), padx=(15, 15))

radb2 = tk.Radiobutton(panel, text='Введення даних', variable=var, value=2, font=('Calibri', 25, 'bold'), bg='#977AF9',
                       fg='black', state=tk.NORMAL, width=22, activebackground='#760598', relief=tk.RAISED,
                       bd='5', command=select_method).grid(row=5, column=0, pady=(10, 10), padx=(15, 15))

# Win 2

labelfr1 = tk.Label(panel2, text="Завдання:", font=('Calibri', 25, 'bold'), bg='#252425', fg='white')

image = Image.open(resource_path("image.png"))
resized_image = image.resize((890, 125))
photo = ImageTk.PhotoImage(resized_image)
label_photo = tk.Label(panel2, image=photo)
label_photo.image = photo

# Win 3

def gauss_elimination(matrix, b):
    n = len(matrix)

    # Forward elimination
    for i in range(n):
        if matrix[i][i] == 0:
            return None  # Singular matrix
        for j in range(i+1, n):
            ratio = matrix[j][i] / matrix[i][i]
            for k in range(n):
                matrix[j][k] -= ratio * matrix[i][k]
            b[j] -= ratio * b[i]

    # Back substitution
    x = [0] * n
    for i in range(n-1, -1, -1):
        x[i] = b[i] / matrix[i][i]
        for j in range(i-1, -1, -1):
            b[j] -= matrix[j][i] * x[i]

    return x

def load_data():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        try:
            with open(file_path, "r") as file:
                data_A1 = file.read().splitlines()
                for i, entry in enumerate(entries):
                    if i < len(data_A1):
                        entry.delete(0, tk.END)
                        entry.insert(0, data_A1[i])
                    else:
                        break
        except FileNotFoundError:
            messagebox.showerror(title='Помилка', message="Файл з даними не знайденно!")
        except IOError:
            messagebox.showerror(title='Помилка', message="Помилка при читанні файлу!")
    else:
        messagebox.showwarning(title='Попередження', message="Ви не обрали файл!")

def solve():
    matrix = []
    for i in range(3):
        row = []
        for j in range(4):
            try:
                value = float(entries[i*4 + j].get())  # Зміщення на і*4 + j
                row.append(value)
            except ValueError:
                messagebox.showerror("Error", "Invalid input")
                return
        matrix.append(row)

    # Розділяємо матрицю на саму матрицю і стовпець вільних членів
    A = [row[:3] for row in matrix]
    b = [row[3] for row in matrix]

    result = gauss_elimination(A, b)
    if result:
        result_text.config(text="x1: {:.2f}, x2: {:.2f}, x3: {:.3f}".format(*result))
    else:
        messagebox.showerror("Error", "Singular matrix")


# Label
labelfr2 = tk.Label(panel3, text="Заповніть матрицю:", font=('Calibri', 25, 'bold'), bg='#252425', fg='white')
result_text = tk.Label(panel3, text="", font=('Calibri', 25, 'bold'), bg='#252425', fg='white')
#Entry
matrix1 = tk.Entry(panel3, font=('Calibri', 20, 'bold'), bg='#5A5A5A', fg='white', width=10)
matrix2 = tk.Entry(panel3, font=('Calibri', 20, 'bold'), bg='#5A5A5A', fg='white', width=10)
matrix3 = tk.Entry(panel3, font=('Calibri', 20, 'bold'), bg='#5A5A5A', fg='white', width=10)
matrix4 = tk.Entry(panel3, font=('Calibri', 20, 'bold'), bg='#5A5A5A', fg='white', width=10)
matrix5 = tk.Entry(panel3, font=('Calibri', 20, 'bold'), bg='#5A5A5A', fg='white', width=10)
matrix6 = tk.Entry(panel3, font=('Calibri', 20, 'bold'), bg='#5A5A5A', fg='white', width=10)
matrix7 = tk.Entry(panel3, font=('Calibri', 20, 'bold'), bg='#5A5A5A', fg='white', width=10)
matrix8 = tk.Entry(panel3, font=('Calibri', 20, 'bold'), bg='#5A5A5A', fg='white', width=10)
matrix9 = tk.Entry(panel3, font=('Calibri', 20, 'bold'), bg='#5A5A5A', fg='white', width=10)
matrix10 = tk.Entry(panel3, font=('Calibri', 20, 'bold'), bg='#5A5A5A', fg='white', width=10)
matrix11 = tk.Entry(panel3, font=('Calibri', 20, 'bold'), bg='#5A5A5A', fg='white', width=10)
matrix12 = tk.Entry(panel3, font=('Calibri', 20, 'bold'), bg='#5A5A5A', fg='white', width=10)

entries = [matrix1, matrix2, matrix3, matrix4, matrix5, matrix6, matrix7, matrix8, matrix9, matrix10, matrix11, matrix12]

#Button
open_button = tk.Button(panel3, text="Завантажити дані", font=('Calibri', 25, 'bold'), bg='#977AF9',
                        relief=tk.RAISED, activebackground='#760598', bd=5, fg='white', command=load_data)
solve_button = tk.Button(panel3, text="Розв'язати", font=('Calibri', 25, 'bold'), bg='#977AF9',
                         relief=tk.RAISED, activebackground='#760598', bd=5, fg='white', command=solve)

win.mainloop()