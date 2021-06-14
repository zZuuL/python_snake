class Item:
    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.__X =  x
        self.__Y =  y

    def __str__(self) -> str:
        return f'{self.__X}, {self.__Y}'

    def __eq__(self, other) -> bool:
        return self.__X == other.X and self.__Y == other.Y

    @property
    def X(self) -> None:
        return self.__X

    @X.setter
    def X(self, x: int) -> None:
        self.__X = x

    @property
    def Y(self) -> None:
        return self.__Y

    @Y.setter
    def Y(self, y: int) -> None:
        self.__Y = y
