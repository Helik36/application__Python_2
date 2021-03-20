from tabulate import tabulate
from work2 import host_range_ping

def host_range_ping_tab():
    # Запрашиваем хосты, проверяем доступность, получаем словарь результатов
    res_dict = host_range_ping()
    print(type(res_dict))
    # выводим в табличном виде
    print(tabulate([res_dict], headers='keys', tablefmt="pipe", stralign='center'))


if __name__ == "__main__":
    host_range_ping_tab()