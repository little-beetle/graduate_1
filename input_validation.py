def correct_login():
    login = input("Введите логин: ")
    if len(login) <= 4:
        print("Логин слишком короткий! Попробуйте еще раз.")
        return correct_login()

    return login


def correct_number(text):
    number = input(text)
    if number.isnumeric():
        return int(number)
    return correct_number(text)

def bank_info(text):
    number = input(text)
    if number.isnumeric():
        if len(number) == 15:
            return int(number)
    return bank_info("Введите ОГРНИП: ")


def bank_info_money(text):
    number = input(text)
    if number.isnumeric():
        if len(number) == 20:
            return int(number)
    return bank_info("Введите ОГРНИП: ")


def correct_name():
    name = input("Введите имя: ")
    if len(name) >= 3 and name.isalpha():
        return name
    print("Ошибка! Попробуйте еще раз.")
    return correct_name()


def correct_age():
    age = input("Введите возраст: ")
    if age.isnumeric():
        if 99 > int(age) > 12:
            return int(age)
    print("Ошибка! Попробуйте еще раз.")
    return correct_age()


def correct_number_phone():
    number_phone = input("Введите номер телефона: ")
    if (number_phone.startswith("+") and len(number_phone) == 13 and number_phone[1:].isnumeric()) or \
            (len(number_phone) == 10 and number_phone.isnumeric()):
        return number_phone
    return correct_number_phone()


def correct_email():
    email = input("Введите адрес электронной почты: ")
    if len(email) >= 7 and email.find("@") != -1 and email.find(".") != -1:
        return email
    print("Ошибка")
    return correct_email()


def correct_index():
    index = input("Введите почтовый индекс: ")
    number_index = []
    for letter in index:
        if letter.isnumeric():
            number_index.append(letter)
    return int("".join(number_index))


def correct_input():
    print("Введите номер пункта меню:", end=" ")
    num = input()
    if num.isnumeric():
        if int(num) <= 2:
            return int(num)
    print("Ошибка!!!")
    return correct_input()