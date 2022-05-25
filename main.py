print('Hola El Mundo')
def summa():
    a = input("Введите первое слово: ")
    b = input("Введите второе слово: ")
    c = input("Введите третье слово: ")

    print(a + " " + b + " " + c)

def my_home_work():
    a = int(input("Введите число А:"))
    b = int(input("Введите число В:"))
    c = int(input("Введите число С:"))

    while a < b:
        print("Грустное сообщение ")
        a = a + c

    print("Радостное сообщение")


my_home_work()
summa()
