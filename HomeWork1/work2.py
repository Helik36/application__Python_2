from ipaddress import ip_address
from Work1 import host_ping


def host_range_ping():
    while True:
        # запрос перваоначального адреса
        start_ip = input("Введите первоначальный адрес: ")
        try:
            # смотрим чему равен последний окте
            las_oct = int(start_ip.split('.')[3])
            break
        except Exception as e:
            print(e)
    while True:
        # Запрос на количество проверяемых адресов
        end_ip = input('Сколько адресов проверить?: ')
        if not end_ip.isnumeric():
            print("Необходимо ввести число: ")
        else:
            # По условию меняется только последний октет
            if (las_oct+int(end_ip)) > 254:
                print(f"Можем только менять только последний октет, т.е "
                      f"максимальное число хотстов для проверки: {254-las_oct}")
            else:
                break

    host_list = []
    #Формируем список ip адресов
    [host_list.append(str(ip_address(start_ip)+x)) for x in range(int(end_ip))]
    # передаём список в функцию из задания 1 для проверки доступности
    return host_ping(host_list)

if __name__ == '__main__':
    host_range_ping()













