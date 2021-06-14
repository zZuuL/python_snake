from item import *
from data import *

class Snake:
    '''
    Snake main class
    '''

    def __init__(self, x: int, y: int, direction: Direction) -> None:
        self.__items = list()
        self.__items.append(Item(x, y))
        for i in range(1, Config.SNAKE_START_SIZE):
            if direction == Direction.Up:
                self.__items.append(Item(x, y + i))
            elif direction == Direction.Down:
                self.__items.append(Item(x, y - i))
            elif direction == Direction.Left:
                self.__items.append(Item(x + i, y))
            elif direction == Direction.Right:
                self.__items.append(Item(x - i, y))

    def __len__(self) -> int:
        return len(self.__items)

    def __getitem__(self, index: int) -> Item:
        if index > len(self):
            raise IndexError()
        return self.__items[index]

    def add(self, item: Item) -> None:
        self.__items.append(item)

    def move(self, direction: Direction) -> Item:
        '''
        Move snake
        '''

        head_item = Item (self.__items[0].X, self.__items[0].Y)
        tail_item = Item (self.__items[len(self.__items) - 1].X, self.__items[len(self.__items) - 1].Y)

        if direction == Direction.Up:
            head_item.Y = Config.HEIGTH if head_item.Y == 1 else head_item.Y - 1
        elif direction == Direction.Down:
            head_item.Y = 1 if head_item.Y == Config.HEIGTH else head_item.Y + 1
        elif direction == Direction.Left:
            head_item.X = Config.WIDTH if head_item.X == 1 else head_item.X - 1
        elif direction == Direction.Right:
            head_item.X = 1 if head_item.X == Config.WIDTH else head_item.X + 1

        if head_item not in self.__items:
            self.__items = [head_item] + self.__items[:-1]
        else:
            raise SnakeCrashException()

        return head_item, tail_item
