# class design:
#game rules: takes user input, initializes board
#grid object
#block super class that can either be subclass'd to nothing, a value that represents numbers and a bomb
from pprint import pprint
import random

class Block:
    def __init__(self, x_value, y_value):
        self.x_value = x_value
        self.y_value = y_value

    def get_value(self):
        pass

    def get_coords(self):
        print(f"{self.x_value} : {self.y_value}")

class Bomb(Block):
    def get_value(self):
        return "BOMB"

class Empty(Block):
    def get_value(self):
        return "Empty"
    
class Indicator(Block):
    def __init__(self, x_value, y_value, number):
        self.x_value = x_value
        self.y_value = y_value
        self.number = number

    def get_value(self):
        return "Indicator"

    def get_number(self):
        return self.number


class Board:
    def __init__(self, size):
        self.size = size
        self.grid = [[None] * size for _ in range(size)]

        for i in range(self.size):
            for j in range(self.size):
                empty_instance = Empty(i, j)
                self.grid[i][j] = empty_instance


        amount = round((size*size) * 0.12)
        for i in range(size):
            for j in range(size):
                random_value = random.random()
                if random_value <= 0.12 and amount > 0:
                    block_instance = Bomb(i, j)
                    self.grid[i][j] = block_instance
                    amount = amount - 1

                if amount == 0:
                    break
            
            if amount == 0:
                break
    
    

    def print_grid(self):
        for row in self.grid:
            for e in row:
                print ('[' + e.get_value() + ']', end=''),
            print()


board_instance = Board(9)

board_instance.print_grid()