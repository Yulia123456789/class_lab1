from tkinter import *


class Book:
    def __init__(self, title, author, year, genre):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre

    def get_list_inf(self):
        return [self.title, self.author, self.year, self.genre]
    def get_inf_dict(self):
        return {'Имя автора': self.author, 'Название книги': self.title, 'Год издания книги': self.year, 'Жанр книги': self.genre}
    def get_inf_str(self):
        return f"Имя автора: {self.author}, Название книги: {self.title}, Год издания книги: {self.year}, Жанр книги: {self.genre}"
def text_box_func(message):
    text_box = Text(window, width=130, height=20, font=("Arial", 10), background='#FFE4E1', foreground='#0A0A0A')

    text_box.grid(row=5, column=0, ipadx=10, ipady=10, padx=10, pady=10, columnspan= 2)
    text_box.insert('end', message)
    text_box.config(state='disabled')



def search_book():
    def save_massage():
        global global_inf_about_book
        root.withdraw()
        entr_dict = {'Имя автора': entr1_range.get(), 'Название книги': entr2_range.get(), 'Год издания книги': entr3_range.get(),
         'Жанр книги': entr4_range.get()}
        message = ""
        for book in global_inf_about_book:
            c = 0
            for entr in entr_dict:
                if entr_dict[entr] != '' and entr_dict[entr] == book.get_inf_dict()[entr]:
                    c += 1
                elif entr_dict[entr] != '' and entr_dict[entr] != book.get_inf_dict()[entr]:
                    c = 0
                    break
            if c != 0:
                message += f'{book.get_inf_str()} \n'
        if message == '':
            message = 'отсутствует'
        text_box_func(message)
    root = Tk()
    root.minsize(1050, 1050)
    root['bg'] = '#FFE4E1'
    text_label = ['Имя автора', 'Название книги', 'Год издания книги', 'Жанр книги']
    k = 0
    for text_lbl in text_label:
        l = Label(root, text=f'{text_lbl}', width=20, height=3, font=("Arial", 14),
                       background='#FFE4E1')
        l.grid(row=0 + k, column=0, columnspan=1)
        k += 1
    entr1_range, entr2_range, entr3_range, entr4_range = Entry(root, width=30), Entry(root, width=30), Entry(root, width=30), Entry(root, width=30)
    entr1_range.grid(row=0, column=1)
    entr2_range.grid(row=1, column=1)
    entr3_range.grid(row=2, column=1)
    entr4_range.grid(row=3, column=1)
    b2_range = Button(root, text='Сохранить', width=20, height=4, background='#EE82EE', foreground='#0A0A0A',
                      font=("Arial", 14))
    b2_range.config(command=save_massage)
    b2_range.grid(row=4, column=1)

    root.mainloop()
def del_book():
    global global_inf_about_book
    global_inf_about_book.clear()
    def save_message2():
        title_book = entr1_range.get()
        for book in library:
            if book.get_list_inf()[0] != title_book:
                global_inf_about_book.append(book)
    root = Tk()
    root.minsize(1050, 1050)
    root['bg'] = '#FFE4E1'
    labl = Label(root, text=f'Название книги', width=20, height=3, font=("Arial", 14),
                       background='#FFE4E1')
    entr1_range = Entry(root, width=30)
    entr1_range.grid(row=0, column=1)
    b2_range = Button(root, text='Сохранить', width=20, height=4, background='#EE82EE', foreground='#0A0A0A', font=("Arial", 14))
    b2_range.config(command=save_message2)
    b2_range.grid(row=4, column=1)
    root.mainloop()

def sort_books():

    def sort1():
        global global_inf_about_book
        message = ""
        s_global_inf_about_book = [i.get_list_inf() for i in global_inf_about_book]
        s_global_inf_about_book.sort(key = lambda book1: book1[1])
        for book2 in s_global_inf_about_book:
            for book in global_inf_about_book:
                if book.get_list_inf() == book2:
                    message += f'{book.get_inf_str()} \n'
        text_box_func(message)
    def sort2():
        global global_inf_about_book
        message = ""
        s_global_inf_about_book = [i.get_list_inf() for i in global_inf_about_book]
        s_global_inf_about_book.sort(key = lambda book1: book1[0])
        for book2 in s_global_inf_about_book:
            for book in global_inf_about_book:
                if book.get_list_inf() == book2:
                    message += f'{book.get_inf_str()} \n'
        text_box_func(message)
    def sort3():
        global global_inf_about_book
        message = ""
        s_global_inf_about_book = [i.get_list_inf() for i in global_inf_about_book]
        s_global_inf_about_book.sort(key = lambda book1: int(book1[2]))
        for book2 in s_global_inf_about_book:
            for book in global_inf_about_book:
                if book.get_list_inf() == book2:
                    message += f'{book.get_inf_str()} \n'
        text_box_func(message)
    def sort4():
        global global_inf_about_book
        message = "-"
        s_global_inf_about_book = [i.get_list_inf() for i in global_inf_about_book]
        s_global_inf_about_book.sort(key = lambda book1: book1[3])
        for book2 in s_global_inf_about_book:
            for book in global_inf_about_book:
                if book.get_list_inf() == book2:
                    message += f'{book.get_inf_str()} \n'
            print(message)
        text_box_func(message)

    root = Tk()
    root.minsize(1050, 1050)
    root['bg'] = '#FFE4E1'
    root.title("Домашняя библиотека")
    text_button = ['Имя автора', 'Название книги', 'Год издания книги', 'Жанр книги']
    func_btn = [sort1, sort2, sort3, sort4]
    r = 0
    for text_btn in text_button:
        b = Button(root, text=f'{text_btn}', width=50, height=4, font=("Arial", 14), background='#FFB6C1',
                   foreground='#0A0A0A')
        func_cmd = func_btn[r]
        b.config(command=func_cmd)
        b.grid(row=0 + r, column=0, ipadx=10, ipady=10, padx=10, pady=10, columnspan=1)
        r += 1

    window.mainloop()
def app_book():
    def save_massage():
        global global_inf_about_book
        root.withdraw()
        book = Book(entr1_range.get(), entr2_range.get(), entr3_range.get(), entr4_range.get())
        global_inf_about_book.append(book)
    root = Tk()
    root.minsize(1050, 1050)
    root['bg'] = '#FFE4E1'
    text_label = ['Имя автора', 'Название книги', 'Год издания книги', 'Жанр книги']
    k = 0
    for text_lbl in text_label:
        l = Label(root, text=f'{text_lbl}', width=20, height=3, font=("Arial", 14),
                       background='#FFE4E1')
        l.grid(row=0 + k, column=0, columnspan=1)
        k += 1
    entr1_range, entr2_range, entr3_range, entr4_range = Entry(root, width=30), Entry(root, width=30), Entry(root, width=30), Entry(root, width=30)
    entr1_range.grid(row=0, column=1)
    entr2_range.grid(row=1, column=1)
    entr3_range.grid(row=2, column=1)
    entr4_range.grid(row=3, column=1)
    b2_range = Button(root, text='Сохранить', width=20, height=4, background='#EE82EE', foreground='#0A0A0A',
                      font=("Arial", 14))
    b2_range.config(command=save_massage)
    b2_range.grid(row=4, column=1)

    root.mainloop()
def show_books():
    global global_inf_about_book
    message = ""
    for book in global_inf_about_book:
        message += f'{book.get_inf_str()} \n'
    text_box_func(message)
def app_inf():
    global global_inf_about_book
    global_inf_about_book = [book1 for book1 in library]


library = [
    Book("1984", "Джордж Оруэлл", "1949", "Дистопия"),
    Book("Убить пересмешника", "Харпер Ли", "1960", "Художественная литература"),
    Book("Великий Гэтсби", "Ф. Скотт Фицджеральд", "1925", "Роман"),
    Book("Моби Дик", "Герман Мелвилл", "1851", "Приключения"),
    Book("Гордость и предубеждение", "Джейн Остин", "1813", "Романтика"),
    Book("Война и мир", "Лев Толстой", "1869", "Исторический роман"),
    Book("Над пропастью во ржи", "Дж.Д. Сэлинджер", "1951", "Художественная литература"),
    Book("Хоббит", "Дж.Р.Р. Толкин", "1937", "Фэнтези"),
    Book("О дивный новый мир", "Олдос Хаксли", "1937", "Дистопия"),
    Book("Преступление и наказание", "Фёдор Достоевский", "1866", "Психологический роман")
]
global_inf_about_book = []
app_inf()

window = Tk()
window.minsize(1050, 1050)
window['bg'] = '#FFE4E1'
window.title("Домашняя библиотека")
text_button = ['Вывести все книги', 'Найти книгу', 'Удалить книгу', 'Сортировать книги', 'Добавить книгу']
func_btn = [show_books, search_book, del_book, sort_books, app_book]
r = 0
for text_btn in text_button:
    b = Button(window, text=f'{text_btn}',width=50, height=4, font=("Arial", 14), background='#FFB6C1', foreground='#0A0A0A')
    func_cmd = func_btn[r]
    b.config(command=func_cmd)
    b.grid(row=0 + r, column=0, ipadx=10, ipady=10, padx=10, pady=10, columnspan=1)
    r += 1

window.mainloop()
