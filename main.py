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
    return correct_input()

# "1 - Ввести или обновить информацию\n" \
#            "\t\n" \
#            "\t\n" \
#            "\t\n" \
#            "2 - Вывести информацию" \
#            "\t\n" \
#            "\t\n" \
#            "\t\n\n" \
#            "0 - Завершить работу"
def input_info():
    print("\t{general_info}\n"
          "\t{businessman_info}\n"
          "\t{back}".format(
        general_info="1 - Общая информация",
        businessman_info="2 - Информация о предпринимателе",
        back="0 - Назад"))


def get_info():
    print("\t{general_info}\n"
          "\t{all_info}\n"
          "\t{back}".format(
        general_info="1 - Общая информацию",
        all_info="2 - Вся информация",
        back="0 - Назад"))

#    return choice
print(title())
menu()
input_info()
get_info()