def title():
    return "Приложение MyProfile\n" \
           "Сохраняй информацию о себе и выводи ее в разных форматах"


def correct_input():
    print("Введите номер пункта меню:", end=" ")
    num = input()
    if num.isnumeric():
        if int(num) <= 2:
            return int(num)
    print("Ошибка!!!")
    return correct_input()



def menu():
    print("{one}\n{two}\n{zero}".format(
        one = "1 - Ввести или обновить информацию",
        two = "2 - Вывести информацию",
        zero = "0 - Завершить работу")
    )
    choice = correct_input()
    return choice


def input_info():
    print("\t{general_info}\n"
          "\t{businessman_info}\n"
          "\t{back}".format(
        general_info="1 - Личная информация",
        businessman_info="2 - Информация о предпринимателе",
        back="0 - Назад"))
    choice = correct_input()
    if choice == 1:
        pass
    elif choice == 2:
        pass
    else:
        return menu()

def get_info():
    print("\t{general_info}\n"
          "\t{all_info}\n"
          "\t{back}".format(
        general_info="1 - Личная информация",
        all_info="2 - Вся информация",
        back="0 - Назад"), end=" ")
    choice = correct_input()
    if choice == 1:
        pass
    elif choice == 2:
        pass
    else:
        return menu()


def input_personal_info():
    global login
    personal_info = dict()
    all_personal_info = dict()
    list_info = []
    login_enter = input("Login ")
    all_list = []
    all_personal_info["Личная информация"] = list_info
    all_list.append(all_personal_info)
    list_info.append(personal_info)
    login[login_enter] = all_list
    for key in login.keys():
        if key == login_enter:
            personal_info["Имя"] = input("Введите имя: ")
            personal_info["Возраст"] = input("Введите возраст: ")
            # info_shop["Телефон"] = input("Введите номер телефона: ")
            # info_shop["E-mail"] = input("Введите адрес электронной почты: ")
            # info_shop["Индекс"] = input("Введите почтовый индекс: ")
            # info_shop["Адрес"] = input("Введите почтовый адрес (без индекса)")
            # info_shop["Дополнительная информация"] = input("Введите дополнительную информацию: ")
            for k, v in login.items():

                for i in v[0].keys():
                    if i == "Личная информация":
                        login[login_enter] = all_list
    return login



def input_businessman_info():

    global login
    businessman_info = dict()
    all_info_businessman = dict()
    list_info = []
    all_list = []
    login_enter = input("Login")

    all_info_businessman["Информация о предпренимателе"] = list_info

    print(len(login[login_enter]))
    personal_info = login[login_enter][0]
    print("++++++++++++", personal_info, type(personal_info))
    login[login_enter] = all_list
    for key in login.keys():
        print(key)
        if key == login_enter:
            print(1)
            businessman_info["ОГРНИП"] = input("Введите ОГРНИП: ")  # print("ОГРНИП должен содержать 15 цифр")
            businessman_info["ИНН"] = input("Введите ИНН")
            # info_shop["Р/с"] = input("Введите расчетный счет: ")
            # info_shop["Банк"] = input("Введите название банка: ")
            # info_shop["БИК"] = input("Введите БИК")
            # info_shop["К/с"] = input("Введите корреспондентский счет:")
            list_info.append(businessman_info)
            all_list.append(all_info_businessman)
            for k, v in login.items():
                for i in v[0].keys():
                    print(i)
                    print(3)
                    if i == "Информация о предпренимателе":
                        all_list.insert(0, personal_info)
                        return login




def get_personal_info():
    pass


def get_businessman_info():
    pass


def play():
    print(title())
    choice = menu()
    if choice == 1:
        input_info()
    elif choice == 2:
        get_info()
    else:
        return "Конец!"

login = dict()
name = dict()

input_personal_info()
input_businessman_info()
input_businessman_info()
print("________")
for d in login.items():
    print(d)
#print(play())