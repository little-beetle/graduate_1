from input_validation import *
def title():
    return "Приложение MyProfile\n" \
           "Сохраняй информацию о себе и выводи ее в разных форматах"





def menu():
    print("-"*60)
    print("{one}\n{two}\n{zero}\n".format(
        one = "1 - Ввести или обновить информацию",
        two = "2 - Вывести информацию",
        zero = "0 - Завершить работу")
    )
    choice = correct_input()
    return choice


def input_info(login):
    print("\t{general_info}\n"
          "\t{businessman_info}\n"
          "\t{back}".format(
        general_info="1 - Личная информация",
        businessman_info="2 - Информация о предпринимателе",
        back="0 - Назад"))
    choice = correct_input()
    if choice == 1:
        input_personal_info(login)
    elif choice == 2:
        input_businessman_info(login)
    else:
        return menu()


def get_info(login):
    print("\t{general_info}\n"
          "\t{all_info}\n"
          "\t{back}".format(
        general_info="1 - Личная информация",
        all_info="2 - Вся информация",
        back="0 - Назад"), end=" ")
    choice = correct_input()
    if choice == 1:
        print(info(login, "Личная информация"))
    elif choice == 2:
        print(info(login, "Вся информация"))
    else:
        return menu()


def input_personal_info(login):

    personal_info = dict()
    all_personal_info = dict()
    list_info = []
    all_list = []
    login_enter = correct_login()
    all_personal_info["Личная информация"] = list_info


    personal_info["Имя"] = correct_name()
    personal_info["Возраст"] = correct_age()
    personal_info["Телефон"] = correct_number_phone()
    personal_info["E-mail"] = correct_email()
    personal_info["Индекс"] = correct_index()
    personal_info["Адрес"] = input("Введите почтовый адрес (без индекса)")
    personal_info["Дополнительная информация"] = input("Введите дополнительную информацию: ")

    for key in login.keys():
        if key == login_enter:

            all_list.append(all_personal_info)

            for login_list in login[key]:
                for k in login_list.keys():
                    if k == "Информация о предпренимателе":
                        businessman_info = login_list
                        all_list.append(businessman_info)
            list_info.append(personal_info)
            login[login_enter] = all_list
            for k, v in login.items():
                for i in v[0].keys():
                    if i == "Личная информация":
                        return login


    login[login_enter] = all_list
    for key in login.keys():
        if key == login_enter:

            list_info.append(personal_info)
            all_list.append(all_personal_info)
            for k, v in login.items():

                for i in v[0].keys():
                    if i == "Информация о предпренимателе":
                        login[login_enter] = all_list

    return login


def input_businessman_info(login):
    businessman_info = dict()
    all_info_businessman = dict()
    list_info = []
    all_list = []

    login_enter = correct_login()

    all_info_businessman["Информация о предпренимателе"] = list_info
    businessman_info["ОГРНИП"] = bank_info("Введите ОГРНИП: ") # print("ОГРНИП должен содержать 15 цифр")
    businessman_info["ИНН"] = correct_number("Введите ИНН")
    businessman_info["Р/с"] = bank_info_money("Введите расчетный счет: ")
    businessman_info["Банк"] = input("Введите название банка: ")
    businessman_info["БИК"] = correct_number("Введите БИК")
    businessman_info["К/с"] = correct_number("Введите корреспондентский счет:")
    for i_key in login.keys():

        if i_key == login_enter:
            personal_info = login[login_enter][0]
            login[login_enter] = all_list

            for key in login.keys():

                if key == login_enter:
                    list_info.append(businessman_info)
                    all_list.append(all_info_businessman)

                    for k, v in login.items():

                        for i in v[0].keys():

                            if i == "Информация о предпренимателе":
                                all_list.insert(0, personal_info)
                                return login


    login[login_enter] = all_list

    for key in login.keys():

        if key == login_enter:

            all_list.append(all_info_businessman)
            list_info.append(businessman_info)

            return login


def info(login, setting):
    login_name = correct_login()
    for key in login.keys():
        if login_name == key:
            for personal_info in login[login_name]:
                for answer in personal_info.keys():
                    if setting == "Личная информация":
                        if answer == setting:
                            return personal_info[answer]
                    elif setting == "Вся информация":
                        return login[login_name]

    else:
        return "В базе такой информации еще нету!"



def play():
    login = dict()
    print(title())
    choice = input("нажмите любую кнопку, чтобы начать!!!\n")
    print("choice", choice)
    while choice != 0:
        choice = menu()
        if choice == 1:
            input_info(login)
        elif choice == 2:
            get_info(login)
        else:
            print(login)
            return "Конец!"


print(play())
