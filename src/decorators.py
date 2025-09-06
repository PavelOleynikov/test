def log(filename=None):
    """Декоратор для логирования выполнения функции.
    Если задан filename, лог записывается в файл, иначе выводится в консоль"""

    def decorator(func):
        """Возвращает обёртку, которая логирует выполнение функции func"""

        def wrapper(*args, **kwargs):
            """Обёртка для выполнения функции func с логированием её результата и ошибок"""

            try:
                result = func(*args, **kwargs)
                if filename:
                    file = open(filename, "a", encoding="utf-8")
                    file.write(f"{func.__name__} ok" + "\n")
                    file.close()
                else:
                    print(f"{func.__name__} ok")
                return result

            except Exception as e:
                if filename:
                    file = open(
                        filename, "a", encoding="utf-8"
                    )  # создаём и открываем файл логов
                    file.write(
                        f"{func.__name__} error: {type(e)}. Inputs: {args}, {kwargs}"
                        + "\n"
                    )
                    file.close()
                else:
                    print(f"{func.__name__} error: {type(e)}. Inputs: {args}, {kwargs}")
                raise

        return wrapper

    return decorator


@log()  # вывод в консоль
def my_function(x, y):
    return x + y


my_function(1, 2)


# @log(filename="mylog.txt")  # запись в файл логов
# def my_function(x, y):
#     return x + y
#
#
# my_function("1", 2)
