from math import sqrt


message = (f'Добро пожаловать в самую лучшую программу для вычисления '
           f'квадратного корня из заданного числа')


def calculate_square_root(number):
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calculator(your_number) :
    if your_number <= 0:
        return
    root = calculate_square_root(your_number)
    print(f"Мы вычислили квадратный корень из введённого"
          f"вами числа. Это будет: {root}")


print(message)
calculator(25.5)