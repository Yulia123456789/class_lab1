from tkinter import *


class Subscriber:
    def __init__(self, identification_number, surname, name, patronymic, address, number_card, debit, credit, time_of_long_distance_negotiations, time_of_city_negotiations):
        self.identification_number = identification_number
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.address = address
        self.number_card = number_card
        self.debit = debit
        self.credit = credit
        self.time_of_long_distance_negotiations = time_of_long_distance_negotiations
        self.time_of_city_negotiations = time_of_city_negotiations

    def values(self, identification_number, surname, name, patronymic, address, number_card, debit, credit, time_of_long_distance_negotiations, time_of_city_negotiations):
        self.identification_number = identification_number
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.address = address
        self.number_card = number_card
        self.debit = debit
        self.credit = credit
        self.time_of_long_distance_negotiations = time_of_long_distance_negotiations
        self.time_of_city_negotiations = time_of_city_negotiations

    def get_values(self):
        return (self.identification_number, self.surname, self.name, self.patronymic, self.address, self.number_card, self.debit, self.credit, self.time_of_long_distance_negotiations, self.time_of_city_negotiations)

    def display_info(self):
        return f"ФИО абонента:{self.surname} {self.name} {self.patronymic}, Адрес: {self.address}, Номер карты: {self.number_card} Кредит: {self.credit}, Дебит: {self.debit}, Междугородные переговоры: {self.time_of_long_distance_negotiations}, Городские переговоры: { self.time_of_city_negotiations}"


abonents = [
    Subscriber(1, "Иванов", "Иван", "Иванович", "Москва, ул. Ленина, д. 1", "1234567890123456", 5000.0, 10000.0, 120, 30),
    Subscriber(2, "Петров", "Алексей", "Алексеевич", "Петербург, ул. Пушкина, д. 10", "2345678901234567", 7000.0, 15000.0, 200, 50),
    Subscriber(3, "Сидоров", "Дмитрий", "Дмитриевич", "Казань, ул. Советская, д. 5", "3456789012345678", 3000.0, 8000.0, 150, 20),
    Subscriber(4, "Михайлов", "Никита", "Никитович", "Новосибирск, ул. Лермонтова, д. 12", "4567890123456789", 9000.0, 20000.0, 180, 0),
    Subscriber(5, "Кузнецов", "Роман", "Романович", "Самара, ул. Куйбышева, д. 15", "5678901234567890", 10000.0, 25000.0, 100, 10),
    Subscriber(6, "Васильев", "Олег", "Викторович", "Екатеринбург, ул. Чкалова, д. 3", "6789012345678901", 4500.0, 12000.0, 75, 60),
    Subscriber(7, "Попов", "Максим", "Игоревич", "Ростов-на-Дону, ул. Мира, д. 8", "7890123456789012", 6000.0, 17000.0, 95, 35),
    Subscriber(8, "Соколова", "Елена", "Александровна", "Волгоград, ул. Герцена, д. 20", "8901234567890123", 8000.0, 22000.0, 50, 25),
    Subscriber(9, "Фёдоров", "Павел", "Сергеевич", "Воронеж, ул. Кирова, д. 7", "9012345678901234", 11000.0, 30000.0, 0, 0),
    Subscriber(10, "Белов", "Игорь", "Петрович", "Краснодар, ул. Победы, д. 5", "0123456789012345", 6500.0, 19000.0, 135, 45),
    Subscriber(11, "Чернов", "Евгений", "Анатольевич", "Томск, ул. Транспортная, д. 9", "1234567890123456", 7500.0, 16000.0, 115, 75),
    Subscriber(12, "Александров", "Виктор", "Михайлович", "Рязань, ул. Дружбы, д. 2", "2345678901234567", 12000.0, 35000.0, 0, 90),
    Subscriber(13, "Дмитриев", "Сергей", "Иванович", "Омск, ул. Ленина, д. 20", "3456789012345678", 5500.0, 13000.0, 200, 0),
    Subscriber(14, "Ларин", "Юрий", "Викторович", "Челябинск, ул. Пушкина, д. 25", "4567890123456789", 8000.0, 21000.0, 0, 110),
    Subscriber(15, "Королёв", "Станислав", "Юрьевич", "Уфа, ул. Герцена, д. 35", "5678901234567890", 12000.0, 30000.0, 150, 40)
]

def text_box_func(message):

    text_box = Text(window, width=180, height=20, font=("Arial", 10), background='#FFE4E1', foreground='#0A0A0A')

    text_box.grid(row=3, column=0, ipadx=10, ipady=10, padx=10, pady=10, columnspan= 3)
    text_box.insert('end', message)
    text_box.config(state='disabled')

def set_range():
    def show_range():
        time_city_negotiations = entr1_range.get()
        message = ""
        for abonent in abonents:
            if int(abonent.time_of_city_negotiations) > int(time_city_negotiations):
                message += f'{abonent.display_info()} \n'
        text_box_func(message)

    lbl0_range = Label(window, text='Введите время городских переговоров', width=50, height=5, font=("Arial", 14), background='#FFE4E1')
    lbl0_range.grid(row=0, column=1)
    entr1_range = Entry(window, width=10)
    entr1_range.grid(row=1, column=1)
    b2_range = Button(window, text='Сохранить', width=20, height=4, background='#EE82EE', foreground='#0A0A0A', font=("Arial", 14))
    b2_range.config(command=show_range)
    b2_range.grid(row=2, column=1)
def filter_long_distance():
    time_abonents = [abonent.display_info() for abonent in abonents if int(abonent.time_of_long_distance_negotiations) > 0]
    message = ""
    for abonent2 in time_abonents:
            message += f'{abonent2} \n'
    text_box_func(message)

def sort_subscriber():
    message = ""
    inf_abn = []
    for abonent in abonents:
        inf_abn.append(abonent.get_values())
    inf_abn.sort(key=lambda abonent: (abonent[1], abonent[2], abonent[3]))

    for abonent2 in inf_abn:
        v = ''
        for j in abonent2:
            v += str(j) + "  "
        message += v + '\n'
    text_box_func(message)

window = Tk()
window.minsize(2050, 2050)
window ['bg'] = '#FFE4E1'
window.grid_columnconfigure(0, weight=0)

text_button = ['Задать время городских переговоровю \n и вывести сведения об абонентвах', 'Абоненты, которые пользовались междугородной связью', 'Список абонентов в алфавитном порядке']
func_btn = [set_range, filter_long_distance, sort_subscriber]
r = 0
for text_btn in text_button:
    b = Button(window, text=f'{text_btn}',width=50, height=4, font=("Arial", 14),
                     background='#FFB6C1', foreground='#0A0A0A')
    func_cmd = func_btn[r]
    b.config(command=func_cmd)
    b.grid(row=0 + r, column=0, ipadx=10, ipady=10, padx=10, pady=10, columnspan=1)
    r += 1

window.mainloop()