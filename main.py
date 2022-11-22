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
    info_shop = dict()
    name_y = dict()
    list_info = []
    login_enter = input("Login")
    all_list = []
    login[login_enter] = all_list
    name_y["Личная информация"] = list_info
    info_shop["Имя"] = input("Введите имя: ")
    info_shop["Возраст"] = input("Введите возраст: ")
    # info_shop["Телефон"] = input("Введите номер телефона: ")
    # info_shop["E-mail"] = input("Введите адрес электронной почты: ")
    # info_shop["Индекс"] = input("Введите почтовый индекс: ")
    # info_shop["Адрес"] = input("Введите почтовый адрес (без индекса)")
    # info_shop["Дополнительная информация"] = input("Введите дополнительную информацию: ")
    list_info.append(info_shop)
    all_list.append(name_y)
    return login



def input_businessman_info():
    global login
    info_shop = dict()
    name_y = dict()
    list_info = []
    login_enter = input("Login")
    all_list = []
    for i in login.keys():
        if i == login_enter:

            try:
                for j in login[i][0].keys():
                    if j != "Информация о предпренимателе":
                        print("YES")
                        all_list.append(login[i])
            except:
                for j in login[i][0][0].keys():
                    print(login[i][0][0])
                    print(type(login[i][0][0]))
                    if j != "Информация о предпренимателе":
                        print("YES")
                        all_list.append(login[i])
    login[login_enter] = all_list
    name_y["Информация о предпренимателе"] = list_info
    info_shop["ОГРНИП"] = input("Введите ОГРНИП: ") #print("ОГРНИП должен содержать 15 цифр")
    info_shop["ИНН"] = input("Введите ИНН")
    # info_shop["Р/с"] = input("Введите расчетный счет: ")
    # info_shop["Банк"] = input("Введите название банка: ")
    # info_shop["БИК"] = input("Введите БИК")
    # info_shop["К/с"] = input("Введите корреспондентский счет:")


    list_info.append(info_shop)
    all_list.append(name_y)
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
print(input_personal_info())
print(input_businessman_info())
print(input_businessman_info())
#print(play())