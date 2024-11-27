from tkinter import *


class Buyer:

    def __init__(self, last_name, name, patronymic, address, number_credit_card, number_bank_balance):
        self.last_name = last_name
        self.name = name
        self.patronymic = patronymic
        self.address = address
        self.number_credit_card = number_credit_card
        self.number_bank_balance = number_bank_balance

    def get_values(self):
        return (self.last_name, self.name, self.patronymic, self.address, self.number_credit_card, self.number_bank_balance)

    def display_info(self):
        return f"ФИО абонента:{self.last_name} {self.name} {self.patronymic}, Адрес: {self.address}, Номер карты: {self.number_credit_card} Номер банковского счета: {self.number_bank_balance}"


buyers = [
    Buyer("Иванов", "Иван", "Иванович", "ул. Пушкина, д. 1", 1234567812345678, "4081781000000001"),
    Buyer("Петров", "Петр", "Петрович", "ул. Лермонтова, д. 2", 2345678923456789, "4081781000000002"),
    Buyer("Сидоров", "Сидор", "Сидорович", "ул. Толстого, д. 3", 3456789034567890, "4081781000000003"),
    Buyer("Зайцева", "Анна", "Петровна", "ул. Чехова, д. 4", 4567890145678901, "4081781000000004"),
    Buyer("Кузнецова", "Елена", "Александровна", "ул. Гоголя, д. 5", 5678901256789012, "4081781000000005"),
    Buyer("Михайлов", "Максим", "Андреевич", "ул. Белинского, д. 6", 6789012367890123, "4081781000000006"),
    Buyer("Федоров", "Алексей", "Владимирович", "ул. Достоевского, д. 7", 7890123478901234, "4081781000000007"),
    Buyer("Смирнова", "Марина", "Сергеевна", "ул. Некрасова, д. 8", 8901234589012345, "4081781000000008"),
    Buyer("Тимофеева", "Ольга", "Александровна", "ул. Толстого, д. 9", 9012345690123456, "4081781000000009"),
    Buyer("Васильева", "Татьяна", "Игоревна", "ул. Чехова, д. 10", 8123456701234567, "4081781000000010"),
    Buyer("Дмитриев", "Дмитрий", "Сергеевич", "ул. Пушкина, д. 11", 1234567812345679, "4081781000000011"),
    Buyer("Григорьева", "Елена", "Вячеславовна", "ул. Лермонтова, д. 12", 2345678923456790, "4081781000000012"),
    Buyer("Ковалев", "Руслан", "Викторович", "ул. Гоголя, д. 13", 3456789034567891, "4081781000000013"),
    Buyer("Яковлева", "Светлана", "Николаевна", "ул. Ломоносова, д. 14", 4567890145678902, "4081781000000014"),
    Buyer("Марков", "Григорий", "Дмитриевич", "ул. Рахманинова, д. 15", 5678901256789013, "4081781000000015"),
    Buyer("Соколова", "Инна", "Станиславовна", "ул. Жукова, д. 16", 6789012367890124, "4081781000000016"),
    Buyer("Левина", "Татьяна", "Геннадиевна", "ул. Васильева, д. 17", 7890123478901235, "4081781000000017"),
    Buyer("Воронова", "Наталья", "Юрьевна", "ул. Льва Толстого, д. 18", 8901234589012346, "4081781000000018"),
    Buyer("Петрова", "Светлана", "Валентиновна", "ул. Пушкина, д. 19", 9012345690123457, "4081781000000019")
]

def text_box_func(message):

    text_box = Text(window, width=110, height=30, font=("Arial", 10), background='#FFE4E1', foreground='#0A0A0A')

    text_box.grid(row=3, column=0, ipadx=10, ipady=10, padx=10, pady=10, columnspan= 2)
    text_box.insert('end', message)
    text_box.config(state='disabled')


def sort_name():
    message = ""
    inf_buyer = []
    for buyer in buyers:
        inf_buyer.append(buyer.get_values())
    print(inf_buyer)
    inf_buyer.sort(key=lambda buyer1: (buyer1[0], buyer1[1], buyer1[2]))

    for buyer2 in inf_buyer:
        v = ''
        for j in buyer2:
            v += str(j) + "  "
        message += v + '\n'
    text_box_func(message)


def range_number_card():
    def show_range_number_card():
        number_credit_card_range1 = entr1_range.get()
        number_credit_card_range2 = entr2_range.get()
        message = ""
        for buyer in buyers:
            if (int(number_credit_card_range1) <= buyer.number_credit_card) and (buyer.number_credit_card <= int(number_credit_card_range2)):
                message += f'{buyer.display_info()} \n'
        print(message)
        text_box_func(message)

    root = Tk()
    root.minsize(1050, 1050)
    root['bg'] = '#FFE4E1'
    lbl0_range = Label(root, text='Введите минимальный диапазон номера карты ', width=50, height=2, font=("Arial", 14), background='#FFE4E1') #40000000000000000
    lbl0_range.grid(row=0, column=2, rowspan=1)
    entr1_range = Entry(root, width=30)
    entr1_range.grid(row=1, column=2, rowspan=1)
    lbl1_range = Label(root, text='Введите максимальный диапазон номера карты ', width=50, height=2, font=("Arial", 14), background='#FFE4E1')
    lbl1_range.grid(row=2, column=2, rowspan=1)
    entr2_range = Entry(root, width=30)
    entr2_range.grid(row=3, column=2, rowspan=1)

    b2_range = Button(root, text='Сохранить', width=20, height=2, font=("Arial", 10), background='#EE82EE', foreground='#0A0A0A')
    b2_range.config(command=show_range_number_card)
    b2_range.grid(row=4, column=2, rowspan=1)

window = Tk()
window.minsize(1050, 1050)
window['bg'] = '#FFE4E1'

text_button = ['Вывести список покупателей \n в алфавитном порядке', 'список покупателей, у которых номер кредитной карточки \n находится в заданном диапазоне']
func_btn = [sort_name, range_number_card]
r = 0
for text_btn in text_button:
    b = Button(window, text=f'{text_btn}',width=50, height=4, font=("Arial", 14), background='#FFB6C1', foreground='#0A0A0A')
    func_cmd = func_btn[r]
    b.config(command=func_cmd)
    b.grid(row=0 + r, column=0, ipadx=10, ipady=10, padx=10, pady=10, columnspan=1)
    r += 1

window.mainloop()

