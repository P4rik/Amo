import os.path
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import math

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
        labelfr1.grid(row=0, column=1, columnspan=7, padx=(10, 10), pady=(0, 0), sticky="snew")
        A1.grid(row=4, column=2, padx=(20, 0), pady=(15, 0))
        B1.grid(row=4, column=4, padx=(20, 0), pady=(15, 0))
        label_photo1.grid(row=1, rowspan=3, column=1, columnspan=7)
        # Entry
        vA1.grid(row=4, column=3, padx=(0, 20), pady=(15, 0), sticky='ew')
        vB1.grid(row=4, column=5, padx=(0, 20), pady=(15, 0), sticky='ew')
        # Button
        button_load1A.grid(row=5, column=3, pady=(40, 0), padx=(0, 20), sticky="snew")
        button_load1B.grid(row=5, column=5, pady=(40, 0), padx=(0, 20), sticky="snew")
        button_res1.grid(row=6, column=3, pady=(40, 0), padx=(0, 20), sticky="snew")
        button_clear1.grid(row=6, column=5, pady=(40, 0), padx=(0, 20), sticky="snew")
    else:
        labelfr1.grid_forget()
        A1.grid_forget()
        B1.grid_forget()
        label_photo1.grid_forget()
        vA1.grid_forget()
        vB1.grid_forget()
        button_load1A.grid_forget()
        button_load1B.grid_forget()
        button_res1.grid_forget()
        button_clear1.grid_forget()
    if method == 2:
        # Labels
        labelfr2.grid(row=0, column=1, columnspan=7, padx=(10, 10), pady=(30, 30), sticky="snew")
        label_photo2.grid(row=1, rowspan=3, column=1, columnspan=7)
        A2.grid(row=4, column=2, padx=(20, 0), pady=(15, 0))
        B2.grid(row=4, column=4, padx=(20, 0), pady=(15, 0))
        C2.grid(row=4, column=6, padx=(20, 0), pady=(15, 0))
        # Entry
        vA2.grid(row=4, column=3, padx=(0, 20), pady=(15, 0), sticky='ew')
        vB2.grid(row=4, column=5, padx=(0, 20), pady=(15, 0), sticky='ew')
        vC2.grid(row=4, column=7, padx=(0, 20), pady=(15, 0), sticky='ew')
        # Button
        button_load2A.grid(row=5, column=3, pady=(40, 0), padx=(0, 20), sticky="snew")
        button_load2B.grid(row=5, column=5, pady=(40, 0), padx=(0, 20), sticky="snew")
        button_load2C.grid(row=5, column=7, pady=(40, 0), padx=(0, 20), sticky="snew")
        button_res2.grid(row=6, column=3, pady=(40, 0), padx=(0, 20), sticky="snew")
        button_clear2.grid(row=6, column=5, pady=(40, 0), padx=(0, 20), sticky="snew")
    else:
        labelfr2.grid_forget()
        label_photo2.grid_forget()
        A2.grid_forget()
        B2.grid_forget()
        C2.grid_forget()
        vA2.grid_forget()
        vB2.grid_forget()
        vC2.grid_forget()
        button_load2A.grid_forget()
        button_load2B.grid_forget()
        button_load2C.grid_forget()
        button_res2.grid_forget()
        button_clear2.grid_forget()
    if method == 3:
        # Labels
        labelfr3.grid(row=0, column=1, columnspan=7, padx=(10, 10), pady=(30, 30), sticky="snew")
        label_photo3.grid(row=1, rowspan=3, column=1, columnspan=7)
        A3.grid(row=4, column=2, padx=(20, 0), pady=(15, 0))
        N3.grid(row=4, column=4, padx=(20, 0), pady=(15, 0))
        # Entry
        vA3.grid(row=4, column=3, padx=(0, 20), pady=(15, 0), sticky='ew')
        vN3.grid(row=4, column=5, padx=(0, 20), pady=(15, 0), sticky='ew')
        # Button
        button_load3A.grid(row=5, column=3, pady=(40, 0), padx=(0, 20), sticky="snew")
        button_load3N.grid(row=5, column=5, pady=(40, 0), padx=(0, 20), sticky="snew")
        button_res3.grid(row=6, column=3, pady=(40, 0), padx=(0, 20), sticky="snew")
        button_clear3.grid(row=6, column=5, pady=(40, 0), padx=(0, 20), sticky="snew")
    else:
        labelfr3.grid_forget()
        label_photo3.grid_forget()
        A3.grid_forget()
        N3.grid_forget()
        vA3.grid_forget()
        vN3.grid_forget()
        button_load3A.grid_forget()
        button_load3N.grid_forget()
        button_res3.grid_forget()
        button_clear3.grid_forget()

#Win 1
win = tk.Tk()
photo = tk.PhotoImage(file=(resource_path('icon.png')))
win.iconphoto(False, photo)
win.title("Вікно 1")
win.config(bg='#363636')
win.geometry("")
win.resizable(False, False)

G = 24
N = 20

#frame
panel = tk.Frame(win, bg='#252425', relief=tk.RAISED, bd=5).grid(row=0, rowspan=11, column=0, sticky='snew')
panel2 = tk.Frame(win, bg='#252425', relief=tk.RAISED, bd=5).grid(row=0, rowspan=11, columnspan=9, column=1,
                                                                  sticky='snew')
panel3 = tk.Frame(win, bg='#252425', relief=tk.RAISED, bd=5).grid(row=0, rowspan=11, column=1, sticky='snew')
panel4 = tk.Frame(win, bg='#252425', relief=tk.RAISED, bd=5).grid(row=0, rowspan=11, column=1, sticky='snew')

#Label
labelname = tk.Label(panel, text=f'Паровенко Данило Едуардович\nМоя група: ІО-{G}\nМій варіант: {N}',
                     bg='#252425', fg='white',
                     font=('Calibri', 20, 'bold')).grid(row=9, column=0, padx=(20, 20), pady=(145, 20))

label_1 = tk.Label(panel, text='Панель керування:', font=('Calibri', 25, 'bold'), bg='#252425', fg='white',
                   height=0).grid(row=0, column=0, padx=(10, 10), pady=(30, 30))

#Radbut
var = tk.IntVar()
radb1 = tk.Radiobutton(panel, text='Лінійний',variable=var, value=1, font=('Calibri', 25, 'bold'), bg='#977AF9',
                       fg='black', state=tk.NORMAL, width=15, activebackground='#760598', relief=tk.RAISED,
                       bd='5', command=select_method).grid(row=1, column=0, pady=(10, 10))

radb2 = tk.Radiobutton(panel, text='Розгалудження',variable=var, value=2, font=('Calibri', 25, 'bold'), bg='#977AF9',
                       fg='black', state=tk.NORMAL, width=15, activebackground='#760598', relief=tk.RAISED,
                       bd='5', command=select_method).grid(row=2, column=0, pady=(10, 10))

radb3 = tk.Radiobutton(panel, text='Циклічний',variable=var, value=3, font=('Calibri', 25, 'bold'), bg='#977AF9',
                       fg='black', state=tk.NORMAL, width=15, activebackground='#760598', relief=tk.RAISED,
                       bd='5', command=select_method).grid(row=3, column=0, pady=(10, 10))

#win 4
def load_data_for_A3():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        try:
            with open(file_path, "r") as file:
                data_A3 = file.read()
                vA3.delete(0, tk.END)
                vA3.insert(0, data_A3)
        except FileNotFoundError:
            messagebox.showerror(title='Помилка', message="Файл з даними A не знайденно!")
        except IOError:
            messagebox.showerror(title='Помилка', message="Помилка при читанні файлу A!")
    else:
        messagebox.showwarning(title='Попередження', message="Ви не обрали файл!")


def load_data_for_N3():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        try:
            with open(file_path, "r") as file:
                data_N3 = file.read()
                vN3.delete(0, tk.END)
                vN3.insert(0, data_N3)
        except FileNotFoundError:
            messagebox.showerror(title='Помилка', message="Файл з даними N не знайденно!")
        except IOError:
            messagebox.showerror(title='Помилка', message="Помилка при читанні файлу N!")
    else:
        messagebox.showwarning(title='Попередження', message="Ви не обрали файл!")

def clear_entries3():
    vA3.delete(0, tk.END)
    vN3.delete(0, tk.END)

def calculate_cyclic_algorithm():
    try:
        A = float(vA3.get())
        B = 1
        N = float(vN3.get())

        first_sum = 0
        result = 0

        if not all(isinstance(val, (int, float)) for val in [A, B, N]):
            messagebox.showerror(title='Помилка', message="Будь ласка, введіть числові значення.")
        elif not N.is_integer():
            messagebox.showerror(title='Помилка', message="N має бути цілим числом.")
        elif N <= 0:
            messagebox.showerror(title='Помилка', message="N має бути додатнім числом.")
        elif any(val > 999999 for val in [A, B, N]):
            messagebox.showerror(title='Помилка', message="Неможливо обчислити результат. Перевірте введені значення!")
        else:
            result = cyclic_algorithm(A, B, N)
            messagebox.showinfo(title='Результат', message=f"f = {result}")
    except ValueError:
        messagebox.showerror(title='Помилка', message="Будь ласка, введіть числові значення.")

def cyclic_algorithm(A, B, N):
    first_sum = sum(A for _ in range(int(N)))
    division = first_sum / N
    result = sum(division for _ in range(int(N))) + B
    return result




#label win4
labelfr3 = tk.Label(panel4, text="Циклічний алгоритм:", font=('Calibri', 25, 'bold'), bg='#252425', fg='white',
                    height=0)
A3 = tk.Label(panel4, text='A=', bg='#252425', fg='white', font=('Calibri', 20, 'bold'))
N3 = tk.Label(panel4, text='N=', bg='#252425', fg='white', font=('Calibri', 20, 'bold'))

#Entry win4
vA3 = tk.Entry(panel4, font=('Calibri', 20, 'bold'), bg='#5A5A5A', fg='white')
vN3 = tk.Entry(panel4, font=('Calibri', 20, 'bold'), bg='#5A5A5A', fg='white')

#Button win4
button_load3A = tk.Button(panel4, text='Завантажити дані для А', font=('Calibri', 25, 'bold'), bg='#977AF9',
                          relief=tk.RAISED, activebackground='#760598', bd=5, fg='white', command=load_data_for_A3)
button_load3N = tk.Button(panel3, text='Завантажити дані для N', font=('Calibri', 25, 'bold'), bg='#977AF9',
                              relief=tk.RAISED, activebackground='#760598', bd=5, fg='white', command=load_data_for_N3)
button_res3 = tk.Button(panel4, text='Обрахувати', font=('Calibri', 25, 'bold'), bg='#977AF9', relief=tk.RAISED,
                        activebackground='#760598', bd=5, fg='white', command=calculate_cyclic_algorithm)
button_clear3 = tk.Button(panel4, text='Очистити', font=('Calibri', 25, 'bold'), bg='#977AF9', relief=tk.RAISED,
                          activebackground='#760598', bd=5, fg='white', command=clear_entries3)

#Image win4
image3 = Image.open(resource_path("image3.png"))
resized_image = image3.resize((377, 202))
photo3 = ImageTk.PhotoImage(resized_image)
label_photo3 = tk.Label(panel4, image=photo3)
label_photo3.image = photo3

#win3
def load_data_for_A2():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        try:
            with open(file_path, "r") as file:
                data_A2 = file.read()
                vA2.delete(0, tk.END)
                vA2.insert(0, data_A2)
        except FileNotFoundError:
            messagebox.showerror(title='Помилка', message="Файл з даними A не знайденно!")
        except IOError:
            messagebox.showerror(title='Помилка', message="Помилка при читанні файлу A!")
    else:
        messagebox.showwarning(title='Попередження', message="Ви не обрали файл!")

def load_data_for_B2():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        try:
            with open(file_path, "r") as file:
                data_B2 = file.read()
                vB2.delete(0, tk.END)
                vB2.insert(0, data_B2)
        except FileNotFoundError:
            messagebox.showerror(title='Помилка', message="Файл з даними B не знайденно!")
        except IOError:
            messagebox.showerror(title='Помилка', message="Помилка при читанні файлу B!")
    else:
        messagebox.showwarning(title='Попередження', message="Ви не обрали файл!")

def load_data_for_C2():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        try:
            with open(file_path, "r") as file:
                data_C2 = file.read()
                vC2.delete(0, tk.END)
                vC2.insert(0, data_C2)
        except FileNotFoundError:
            messagebox.showerror(title='Помилка', message="Файл з даними C не знайденно!")
        except IOError:
            messagebox.showerror(title='Помилка', message="Помилка при читанні файлу C!")
    else:
        messagebox.showwarning(title='Попередження', message="Ви не обрали файл!")


def solve_quadratic_equation():
    try:
        a = float(vA2.get())
        b = float(vB2.get())
        c = float(vC2.get())

        D = b ** 2 - 4 * a * c

        if D > 0:
            x1 = (-b + math.sqrt(D)) / (2 * a)
            x2 = (-b - math.sqrt(D)) / (2 * a)

            y1 = a * x1 ** 2 + b * x1 + c
            y2 = a * x2 ** 2 + b * x2 + c

            messagebox.showinfo("Результат", f"x1 = {x1}, y1 = {y1}\nx2 = {x2}, y2 = {y2}")
        else:
            x = -b / (2 * a)
            y = c * x ** 2 - a * x + b

            messagebox.showinfo("Результат", f"x = {x}, y = {y}")
    except ValueError:
        messagebox.showerror("Помилка", "Будь ласка, введіть числові значення.")

def clear_entries2():
    vA2.delete(0, tk.END)
    vC2.delete(0, tk.END)
    vB2.delete(0, tk.END)

#labels win3
labelfr2 = tk.Label(panel3, text="Алгоритм що розгалужується:", font=('Calibri', 25, 'bold'), bg='#252425', fg='white',
                         height=0)
A2 = tk.Label(panel3, text='A=', bg='#252425', fg='white', font=('Calibri', 20, 'bold'))
B2 = tk.Label(panel3, text='B=', bg='#252425', fg='white', font=('Calibri', 20, 'bold'))
C2 = tk.Label(panel3, text='C=', bg='#252425', fg='white', font=('Calibri', 20, 'bold'))
#Entry win3
vA2 = tk.Entry(panel3, font=('Calibri', 20, 'bold'), bg='#5A5A5A', fg='white')
vB2 = tk.Entry(panel3, font=('Calibri', 20, 'bold'), bg='#5A5A5A', fg='white')
vC2 = tk.Entry(panel3, font=('Calibri', 20, 'bold'), bg='#5A5A5A', fg='white')
#Button win3
button_load2A = tk.Button(panel3, text='Завантажити дані для А', font=('Calibri', 25, 'bold'), bg='#977AF9',
                          relief=tk.RAISED, activebackground='#760598', bd=5, fg='white', command=load_data_for_A2)
button_load2B = tk.Button(panel3, text='Завантажити дані для B', font=('Calibri', 25, 'bold'), bg='#977AF9',
                          relief=tk.RAISED, activebackground='#760598', bd=5, fg='white', command=load_data_for_B2)
button_load2C = tk.Button(panel3, text='Завантажити дані для C', font=('Calibri', 25, 'bold'), bg='#977AF9',
                          relief=tk.RAISED, activebackground='#760598', bd=5, fg='white', command=load_data_for_C2)
button_res2 = tk.Button(panel3, text='Обрахувати', font=('Calibri', 25, 'bold'), bg='#977AF9', relief=tk.RAISED,
                        activebackground='#760598', bd=5, fg='white', command=solve_quadratic_equation)
button_clear2 = tk.Button(panel3, text='Очистити', font=('Calibri', 25, 'bold'), bg='#977AF9', relief=tk.RAISED,
                          activebackground='#760598', bd=5, fg='white', command=clear_entries2)
#Image win3
image2 = Image.open(resource_path("image2.png"))
resized_image = image2.resize((377, 202))
photo2 = ImageTk.PhotoImage(resized_image)
label_photo2 = tk.Label(panel3, image=photo2)
label_photo2.image = photo2

#win2
def load_data_for_A1():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        try:
            with open(file_path, "r") as file:
                data_A1 = file.read()
                vA1.delete(0, tk.END)
                vA1.insert(0, data_A1)
        except FileNotFoundError:
            messagebox.showerror(title='Помилка', message="Файл з даними A не знайденно!")
        except IOError:
            messagebox.showerror(title='Помилка', message="Помилка при читанні файлу A!")
    else:
        messagebox.showwarning(title='Попередження', message="Ви не обрали файл!")

def load_data_for_B1():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        try:
            with open(file_path, "r") as file:
                data_B1 = file.read()
                vB1.delete(0, tk.END)
                vB1.insert(0, data_B1)
        except FileNotFoundError:
            messagebox.showerror(title='Помилка', message="Файл з даними B не знайденно!")
        except IOError:
            messagebox.showerror(title='Помилка', message="Помилка при читанні файлу B!")
    else:
        messagebox.showwarning(title='Попередження', message="Ви не обрали файл!")

def calculate_Y1():
    try:
        a = float(vA1.get())
        b = float(vB1.get())
    except ValueError:
        messagebox.showerror("Помилка", "Будь ласка, введіть числові значення.")
        return

    try:
        result = math.log10(math.sqrt(a**2 + b**2)) - math.log(math.sqrt(a**2 - b**2))
    except ValueError:
        messagebox.showerror("Помилка", "Неможливо обчислити результат. Перевірте введені значення!")
        return

    messagebox.showinfo("Результат", f"Y1 = {result}")

def clear_entries1():
    vA1.delete(0, tk.END)
    vB1.delete(0, tk.END)

#labels win2
labelfr1 = tk.Label(panel2, text="Лінійний алгоритм:", font=('Calibri', 25, 'bold'), bg='#252425', fg='white')
A1 = tk.Label(panel2, text='A=', bg='#252425', fg='white', font=('Calibri', 20, 'bold'))
B1 = tk.Label(panel2, text='B=', bg='#252425', fg='white', font=('Calibri', 20, 'bold'))

#Entry win2
vA1 = tk.Entry(panel2, font=('Calibri', 20, 'bold'), bg='#5A5A5A', fg='white')
vB1 = tk.Entry(panel2, font=('Calibri', 20, 'bold'), bg='#5A5A5A', fg='white')

#Button win2
button_load1A = tk.Button(panel2, text='Завантажити дані для А', font=('Calibri', 25, 'bold'), bg='#977AF9',
                          relief=tk.RAISED, activebackground='#760598', bd=5, fg='white', command=load_data_for_A1)
button_load1B = tk.Button(panel2, text='Завантажити дані для B', font=('Calibri', 25, 'bold'), bg='#977AF9',
                          relief=tk.RAISED, activebackground='#760598', bd=5, fg='white', command=load_data_for_B1)
button_res1 = tk.Button(panel2, text='Обрахувати', font=('Calibri', 25, 'bold'), bg='#977AF9', relief=tk.RAISED,
                        activebackground='#760598', bd=5, fg='white', command=calculate_Y1)
button_clear1 = tk.Button(panel2, text='Очистити', font=('Calibri', 25, 'bold'), bg='#977AF9', relief=tk.RAISED,
                          activebackground='#760598', bd=5, fg='white', command=clear_entries1)
#Image win2
image1 = Image.open(resource_path("image1.png"))
resized_image = image1.resize((377, 202))
photo1 = ImageTk.PhotoImage(resized_image)
label_photo1 = tk.Label(panel2, image=photo1)
label_photo1.image = photo1

win.mainloop()