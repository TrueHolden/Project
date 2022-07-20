field = [[' '] * 3 for i in range(3)]
def greetings():
    print('|Приветсвую тебя в игре|')
    print('  |Крестики - Нолики|')
    print()
    print('формат ввода "x и y"')
    print()
    print('где "x" это строка')
    print('а "y" это столбец')
    print('------------------------')
    print()

def show_field():
    print(f'   | 0 | 1 | 2 |')
    print('----------------')
    for i, inf in enumerate(field):
        info = f' {i} | {" | ".join(map(str, inf))} |'
        print(info)
        print('----------------')


def ask_point():
    while True:
        cords = input('Ваш ход,\n введите Координаты через пробел:').split()

        if len(cords) != 2:
            print('Введите 2 координаты!')
            continue

        x, y = cords

        if not(x.isdigit()) or not(y.isdigit()):
            print('Введите числа!')
            continue

        x, y = int(x), int(y)

        if x > 2 or x < 0 or y > 2 or y < 0:
            print('Вы вышли за рамки координат!')
            continue

        if field[x][y] != ' ':
            print('Клетка уже занята!')
            continue

        return x, y


def winner_check():
    win_cord = [((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2))]
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!!!")
            return True
    return False



greetings()
count = 0
while True:
    count += 1

    show_field()

    if count % 2 == 1:
        print('Ходит крестик')
    else:
        print('Ходит нолик')

    x, y = ask_point()

    if count % 2 == 1:
        field[x][y] = 'X'
    else:
        field[x][y] = "0"

    if winner_check():
        break

    if count == 9:
        print('Ничья')
        show_field()
        break

