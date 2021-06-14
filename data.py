from enum import Enum, auto

class SnakeCrashException(Exception): pass


class Direction(Enum):
    Up    = auto(),
    Down  = auto(),
    Left  = auto(),
    Right = auto()


class Colors(Enum):
    Black   = (0, 0, 0)
    Gray_1  = (5, 5, 5)
    Gray_2  = (30, 30, 30)
    White   = (255, 255, 255)
    Green_1 = (11, 213, 31)
    Green_2 = (9, 159, 23)
    Green_3 = (5, 103, 15)
    Green_4 = (3, 69, 10)
    Red     = (223, 0, 5)
    Yellow  = (240, 235, 19)


class Config:
    WIDTH             = 100
    HEIGTH            = 60
    PIXEL_SIZE        = 10

    # WIDTH             = 20
    # HEIGTH            = 20
    # PIXEL_SIZE        = 40

    PIXEL_BORDER_SIZE = 1

    FPS = 3

    SNAKE_HEAD_COLOR = Colors.Green_1
    SNAKE_COLOR      = Colors.Green_4
    SNAKE_START_SIZE = 3
