import tkinter as tk
from tkinter import *
from tkinter import messagebox
import random
from abc import ABC, abstractmethod

class Animal:
    def __init__(self, identifier, name, animal_type):
        self.identifier = identifier
        self.name = name
        self.animal_type = animal_type
        self.food_amount = self.calculate_food()

    @abstractmethod
    def calculate_food(self):
        pass

    def str(self):
        return f"ID: {self.identifier}, Name: {self.name}, Type: {self.animal_type}, Food: {self.food_amount} kg"


class Carnivore(Animal):
    def calculate_food(self):
        return random.randint(5, 20)  # Хищники едят от 5 до 20 кг мяса


class Omnivore(Animal):
    def calculate_food(self):
        return random.randint(3, 10)  # Всеядные едят от 3 до 10 кг пищи


class Herbivore(Animal):
    def calculate_food(self):
        return random.randint(2, 8)  # Травоядные едят от 2 до 8 кг растительности


def read_animals_from_file(filename):
    animals = []
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                parts = line.strip().split(',')
                if len(parts) != 3:
                    raise ValueError(f"Неверный формат данных: {line}")
                identifier, name, animal_type = parts
                if animal_type == "Carnivore":
                    animals.append(Carnivore(identifier, name, animal_type))
                elif animal_type == "Omnivore":
                    animals.append(Omnivore(identifier, name, animal_type))
                elif animal_type == "Herbivore":
                    animals.append(Herbivore(identifier, name, animal_type))
                else:
                    raise ValueError(f"Неизвестный тип животного: {animal_type}")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Ошибка при чтении файла: {e}")
    return animals


def write_animals_to_file(filename, animals):
    try:
        with open(filename, 'w') as file:
            for animal in animals:
                file.write(f"{animal.identifier},{animal.name},{animal.animal_type}\n")
    except Exception as e:
        messagebox.showerror("Ошибка", f"Ошибка при записи в файл: {e}")


def sort_animals(animals):
    return sorted(animals, key=lambda x: (-x.food_amount, x.name))


def display_animals():
    animal_listbox.delete(0, tk.END)
    for animal in animals:
        animal_listbox.insert(tk.END, animal.str())


def save_animals():
    write_animals_to_file("zoo.txt", animals)


def load_animals():
    global animals  # Объявляем, что переменная animals глобальная
    animals = read_animals_from_file("zoo.txt")
    display_animals()


def sort_and_display():
    global animals  # Объявляем, что переменная animals глобальная
    if not animals:
        messagebox.showwarning("Предупреждение", "Сначала загрузите данные.")
        return
    animals = sort_animals(animals)
    display_animals()


def show_first_5():
    if not animals:
        messagebox.showwarning("Предупреждение", "Сначала загрузите данные.")
        return
    first_5 = sorted(animals, key=lambda x: (-x.food_amount, x.name))[:5]
    names = "\n".join([animal.name for animal in first_5])
    messagebox.showinfo("Первые 5 животных", names)


def show_last_3():
    if not animals:
        messagebox.showwarning("Предупреждение", "Сначала загрузите данные.")
        return
    last_3 = sorted(animals, key=lambda x: (-x.food_amount, x.name))[-3:]
    ids = "\n".join([animal.identifier for animal in last_3])
    messagebox.showinfo("Последние 3 ID", ids)


# Функция для добавления нового животного
def add_animal():
    name = animal_name_entry.get()
    animal_type = animal_type_var.get()

    if not name or not animal_type:
        messagebox.showwarning("Предупреждение", "Пожалуйста, заполните все поля.")
        return


    identifier = f"00{str(len(animals) + 1)}"


    if animal_type == "Carnivore":
        new_animal = Carnivore(identifier, name, animal_type)
    elif animal_type == "Omnivore":
        new_animal = Omnivore(identifier, name, animal_type)
    elif animal_type == "Herbivore":
        new_animal = Herbivore(identifier, name, animal_type)

    animals.append(new_animal)
    display_animals()  # Обновляем отображение списка
    messagebox.showinfo("Успех", f"Животное {name} добавлено!")

    # Очистить поле ввода имени после добавления
    animal_name_entry.delete(0, tk.END)


# Глобальные переменные
animals = []


root = Tk()
root.title("Животные")
root['bg'] = '#FFE4E1'


animal_name_label = Label(root, text="Имя животного:", font=("Arial", 12), bg="#FFE4E1")
animal_name_label.pack()
animal_name_entry = Entry(root, font=("Arial", 12))
animal_name_entry.pack()

animal_type_label = Label(root, text="Тип животного:", font=("Arial", 12), bg="#FFE4E1")
animal_type_label.pack()

animal_type_var = StringVar()
animal_type_var.set("Carnivore")

animal_type_menu = OptionMenu(root, animal_type_var, "Carnivore", "Omnivore", "Herbivore")
animal_type_menu.pack()



r1 = 0
funcn = [add_animal, display_animals, load_animals, save_animals, sort_and_display, show_first_5, show_last_3]
text_button = ["Добавить животное","Вывести на экран", "Загрузить из файла", "Сохранить в файл", "Сортировать животных", "Первые 5 животных", "Последние 3 ID"]
for i1 in range(len(text_button)):
    b1 = Button(root, text=f'{text_button[i1]}', width=80, height=3, font=("Arial", 14), background='#FFB6C1', foreground='#0A0A0A')
    cmd = lambda x=i1: funcn[x]()
    b1.config(command=cmd)
    b1.pack()
    r1 += 1

animal_listbox = tk.Listbox(root, width=50, height=15)
animal_listbox.pack()

root.mainloop()