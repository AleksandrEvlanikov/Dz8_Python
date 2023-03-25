from os import path

file_base = "base.txt"
last_id = 0
all_data = []

if not path.exists(file_base):
    with open(file_base, "w", encoding="utf-8") as _:
        pass


def delete_number():
    delcontact = "base.txt"
    with open(delcontact, "r") as d:
        contacts = d.readlines()
    if contacts:
        index = int(input('Введите индекс элемента, который вы хотите удалить: '))
        if 0 <= index < len(contacts):
            del contacts[index]
            with open(delcontact, "w") as d:
                d.writelines(contacts)
        else:
            print('Неверный индекса, введите из списка контактов.')
    else:
        print('Список пуст.')

def update_contacts():
    upcantacts = "base.txt"
    with open(upcantacts, "r") as u:
        contacts = u.readlines()

    index = int(input('Введите индекс элемента, который вы хотите изменить: '))
    if 0 <= index > len(contacts):
        print('Некорректный номер контакта')
        return

    array = ["id", "surname", "name", "patronymic", "phone_number"]
    string = ""
    for i in array:
        while True:
            input_str = input(f"Enter {i} ")
            if i == "id" and not input_str.isdigit():
                print("Введите правильные ID. ")
            elif i == "phone_number" and not input_str.isdigit():
                print("Введите правильный номер. ")
            else:
                string += input_str + " "
                break
    contacts[index] = string + "\n"

    with open(upcantacts, "w") as u:
        u.writelines(contacts)

# def Check_numbers(array, string):
#     for i in array:
#         while True:
#             input_str = input(f"Enter {i} ")
#             if i == "id" and not input_str.isdigit():
#                 print("Введите правильные ID. ")
#             elif i == "phone_number" and not input_str.isdigit():
#                 print("Введите правильный номер. ")
#             else:
#                 string += input_str + " "
#                 break


def search_contact():
    search_data = exist_contact(0, input('Кого ищите? '))
    if search_data:
        print(*search_data, sep="\n")
    else:
        print('Такого нету.')


def exist_contact(rec_id, data):
    if rec_id:
        contact = [i for i in all_data if rec_id in i.split()[0]]
    else:
        contact = [i for i in all_data if data in i]
    return contact


def read_records():
    global last_id, all_data

    with open(file_base, encoding="utf-8") as f:
        all_data = [i.strip() for i in f]
        if all_data:
            last_id = int(all_data[-1].split()[0])
            return all_data
    return []


def show_all():
    if all_data:
        print(*all_data, sep="\n")
    else:
        print("Empty data")


def add_new_contact():
    global last_id
    array = ["surname", "name", "patronymic", "phone_number"]
    string = ""
    for i in array:
        while True:
            input_data = input(f"Enter {i} ") + " "
            if i == "phone_number" and not input_data.strip().isdigit():
                print("Введите правильный номер. ")
            else:
                string += input_data + " "
                break
    last_id += 1
    with open(file_base, "a", encoding="utf-8") as f:
        f.write(f"{last_id} {string}\n")


def main_menu():
    play = True
    while play:
        read_records()
        answer = input("Phone book:\n"
                       "1. Show all records\n"  #  Показать все записи
                       "2. Add a record\n"      #  Добавить запись
                       "3. Search a record\n"   #  Поиск записи
                       "4. Change\n"            #  Изменить
                       "5. Delete\n"            #  Удалить
                       "6. Exp/Imp\n"           #  экспорт\импорт
                       "7. Exit\n")             #  Выход
        match answer:
            case "1":
                show_all()
            case "2":
                add_new_contact()
            case "3":
                search_contact()
            case "4":
                update_contacts()
            case "5":
                delete_number()
            case "6":
                pass
            case "7":
                play = False
            case _:
                print("Try again!\n")


main_menu()