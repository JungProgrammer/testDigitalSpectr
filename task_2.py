from random import randint


class SearchPoint():
    def __init__(self, w, h):
        self.__x = randint(0, w)
        self.__y = randint(0, h)

    def where_is_point(self, x, y):
        """Возможные варианты: "R", "RU", "RD", "L", "LU", "LD", "U", "D"""
        pos_x = pos_y = ''
        if x > self.__x:
            pos_x = 'L'
        elif x < self.__x:
            pos_x = 'R'
        if y > self.__y:
            pos_y = 'D'
        elif y < self.__y:
            pos_y = 'U'
        return pos_x + pos_y


#алгоритм поиска
def SearchMethod(lb, rb, db, ub, x, y, SP):
    left_bord_x = lb
    right_bord_x = rb
    down_bord_y = db
    upper_bord_y = ub

    now_pos = SP.where_is_point(x, y)
    print(x, y)

    if now_pos == '':
        print(f"Искомая точка:{x, y}")
    else:
        if now_pos == 'R':
            left_bord_x = x
            x += (right_bord_x - x) // 2
            SearchMethod(left_bord_x, right_bord_x, down_bord_y, upper_bord_y, x, y, SP)
        elif now_pos == 'L':
            right_bord_x = x
            x -= (x - left_bord_x) // 2
            SearchMethod(left_bord_x, right_bord_x, down_bord_y, upper_bord_y, x, y, SP)
        elif now_pos == 'U':
            down_bord_y = y
            y += (upper_bord_y - y) // 2
            SearchMethod(left_bord_x, right_bord_x, down_bord_y, upper_bord_y, x, y, SP)
        elif now_pos == 'D':
            upper_bord_y = y
            y -= (y - down_bord_y) // 2
            SearchMethod(left_bord_x, right_bord_x, down_bord_y, upper_bord_y, x, y, SP)
        elif now_pos == 'RU':
            left_bord_x = x
            x += (right_bord_x - x) // 2
            down_bord_y = y
            y += (upper_bord_y - y) // 2
            SearchMethod(left_bord_x, right_bord_x, down_bord_y, upper_bord_y, x, y, SP)
        elif now_pos == 'RD':
            left_bord_x = x
            x += (right_bord_x - x) // 2
            upper_bord_y = y
            y -= (y - down_bord_y) // 2
            SearchMethod(left_bord_x, right_bord_x, down_bord_y, upper_bord_y, x, y, SP)
        elif now_pos == 'LU':
            right_bord_x = x
            x -= (x - left_bord_x) // 2
            down_bord_y = y
            y += (upper_bord_y - y) // 2
            SearchMethod(left_bord_x, right_bord_x, down_bord_y, upper_bord_y, x, y, SP)
        elif now_pos == 'LD':
            right_bord_x = x
            x -= (x - left_bord_x) // 2
            upper_bord_y = y
            y -= (y - down_bord_y) // 2
            SearchMethod(left_bord_x, right_bord_x, down_bord_y, upper_bord_y, x, y, SP)


w, h = int(input("Ширина:")), int(input("Высота"))
SP = SearchPoint(w, h)

x = int(input("Координата x стартовой точки"))
y = int(input("Координата y стартовой точки"))
SearchMethod(0, w, 0, h, x, y, SP)
