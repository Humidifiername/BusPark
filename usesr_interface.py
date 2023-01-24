import func_read
import func_save
import time
print("Справочник автобусного парка")

def menu():
    print(
        "1 - Вывод списка автобусов\n"
        "2 - Добавление автобуса и гос номера в список\n"
        "3 - Вывод списка водителей\n"
        "4 - Добавление водителя и его фамилии в список\n"
        "5 - Вывод списка кондукторов\n"
        "6 - Добавление кондуктора в список\n"
        "7 - Вывод списка маршрутов\n"
        "8 - Добавление маршрута в список\n"
        "9 - Выход\n"        
        )
    number_menu = int(input("Введите нужную цифру: "))

    if number_menu == 1:
        func_read.read("Bus.txt")
        time.sleep(3)
        menu()
    elif number_menu == 2:
        func_save.save("Bus.txt", input("Введите идентификатор автобуса и его гос номер через запятую: "))
        time.sleep(1)
        menu()
    elif number_menu == 3:
        func_read.read("Drivers.txt")
        time.sleep(3)
        menu()
    elif number_menu == 4:
        func_save.save("Drivers.txt", input("Введите идентификатор водителя и его фамилию через запятую: "))
        time.sleep(1)
        menu()
    elif number_menu == 5:
        func_read.read("Conductor.txt")
        time.sleep(3)
        menu()
    elif number_menu == 6:
        func_save.save("Conductor.txt", input("Введите идентификатор кондуктора: "))
        time.sleep(1)
        menu()
    elif number_menu == 7:
        func_read.read("Route.txt")
        time.sleep(3)
        menu()
    elif number_menu == 8:
        func_save.save("Route.txt", input("Введите идентификатор маршрута и его номер через запятую: "))
        time.sleep(1)
        menu()
    elif number_menu == 9:
        print("Вы вышли и справочника")
    else:
        print("Такого пункта меню нет")
        menu()
menu()    