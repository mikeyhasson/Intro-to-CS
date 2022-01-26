import helper
from board import Board
from car import Car
import sys


class Game:
    """
    This class represents a Rush-Hour game. It uses objects from the classes Car and Board within it.
    """
    #using duplicate code because it was said each class could be replaced.
    LEGAL_NAMES = ["Y", "B", "O", "W", "G", "R"]
    LEGAL_DIRECTIONS = ['u', 'd', 'l', 'r']
    LEGAL_ORIENTATIONS = [0,1]
    MIN_LENGTH, MAX_LENGTH = 2, 4
    FILENAME_INDEX=1
    EXIT = "!"
    INPUT_LEN=3
    WIN_MSG = "Congrats! You have won the game"
    DIRECTION_INVALID = "Chosen direction is invalid"
    CAR_NAME_INVALID = "Inserted Car name is invalid"
    CAR_ADD_FAIL = "The program has failed to add one of the cars to the board"
    CAR_MOVE_FAILED = "Could not move the car in the requested direction"
    INPUT_FORM_INVALID = "The input inserted is in invalid form"
    INPUT_CAR_MOVE_MSG = "Insert car name and direction is the form name,direction: "

    def __init__(self, board):
        """
        Initialize a new Game object.
        :param board: An object of type board
        """
        self.__board = board

    def play(self):
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """
        print(self.__board)
        flag = True #will be marked False when user reaches the target location.
        while flag:
            user_input = input(Game.INPUT_CAR_MOVE_MSG)
            if user_input == Game.EXIT:#if user inserts the exit string, we go out of the loop
                break
            name, direction = check_input(user_input)#if input is invalid, None will be returned.
            if name is None or direction is None:
                continue

            moved = self.__board.move_car(name, direction)#after checking input, trying to move.
            if not moved:
                print(Game.CAR_MOVE_FAILED)
            else:
                print(self.__board)
                target = self.__board.target_location()
                if self.__board.cell_content(target): #if there is a car in the target location end of game.
                    print(Game.WIN_MSG)
                    flag = False


def check_input(user_input):
    """
    This function checks a user input for each turn in a rush hour game.
    User input is supposed to be in the form NAME,DIRECTION.
    The function checks if it was inserted in a correct way and checks if the name and direction are valid.
    :param user_input:
    :return:
    """
    if len(user_input) == Game.INPUT_LEN and user_input[1] == ",": #checks that length is 3 and there is a comma.
        name, direction = user_input[0], user_input[-1]
    else:
        print(Game.INPUT_FORM_INVALID)
        return None, None
    if name not in Game.LEGAL_NAMES: #checks if name is legal
        print(Game.CAR_NAME_INVALID)
        return None, None
    if direction not in Game.LEGAL_DIRECTIONS:#checks if the direction is legal
        print(Game.DIRECTION_INVALID)
        return None, None
    return name, direction

if __name__ == "__main__":
    new_board = Board()
    filename = sys.argv[Game.FILENAME_INDEX]
    car_data = helper.load_json(filename)
    for car_name in car_data.keys():
        #checking each car in json file, if it is not vallid, skipping car.
        length, location, orientation = car_data[car_name]
        if car_name not in Game.LEGAL_NAMES:
            continue
        if length < Game.MIN_LENGTH or length > Game.MAX_LENGTH or int(length) != length:
            continue
        if orientation not in Game.LEGAL_ORIENTATIONS:
            continue
        #if data is valid, we create a new car object and add it to the board
        new_car = Car(car_name, length, tuple(location), orientation)
        new_board.add_car(new_car)
    game = Game(new_board) #after creating the board, starting game.
    game.play()