from car import Car


class Board:
    """
    This class is meant to represent a gameboard that uses Car objects in it. and has a length of 7.
    """
    # using duplicate code because it was said each class could be replaced.
    OPPOSITE_DIRECTION = {'u': 'd', 'd': 'u', 'r': 'l', 'l': 'r'}
    EXIT_MARK = "E"
    ROW, COLUMN = 0, 1
    EMPTY_CELL = "_"
    TARGET_COORDS = (3, 7)
    DEF_LENGTH = 7

    def __init__(self):
        self.__game_board = []
        for i in range(Board.DEF_LENGTH):
            new_lst = ["_"] * Board.DEF_LENGTH
            if i == Board.DEF_LENGTH // 2:
                new_lst += [Board.EXIT_MARK]
            self.__game_board.append(new_lst)
        self.__cars = []

    def __str__(self):
        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board
        """
        string = ""
        for i in self.__game_board:
            string += str(i) + "\n"
        return string

    def cell_list(self):
        """ This function returns the coordinates of cells in this board
        :return: list of coordinates
        """
        cell_list = []
        for i in range(Board.DEF_LENGTH):
            for j in range(Board.DEF_LENGTH):
                cell_list.append((i, j))
        cell_list.append(Board.TARGET_COORDS)
        return cell_list

    def possible_moves(self):
        """ This function returns the legal moves of all cars in this board
        :return: list of tuples of the form (name,movekey,description)
                 representing legal moves
        """
        legal_lst = []
        for car in self.__cars:
            moves_dict = car.possible_moves()
            for direction in moves_dict.keys():
                coords = car.movement_requirements(direction)[0]
                if self.coord_ok(coords):
                    legal_lst.append((car.get_name(), direction, moves_dict[direction]))
        return legal_lst

    def target_location(self):
        """
        This function returns the coordinates of the location which is to be filled for victory.
        :return: (row,col) of goal location
        """
        return Board.TARGET_COORDS

    def cell_content(self, coordinate):
        """
        Checks if the given coordinates are empty.
        :param coordinate: tuple of (row,col) of the coordinate to check
        :return: The name if the car in coordinate, None if empty
        """
        row = coordinate[Board.ROW]
        column = coordinate[Board.COLUMN]
        content = self.__game_board[row][column]
        if content == "_" or content == "E":
            return None
        else:
            return content

    def coord_ok(self, coords):
        if coords in self.cell_list() and self.cell_content(coords) is None:
            return True

    def fill_coord(self, coords, name):
        row = coords[Board.ROW]
        column = coords[Board.COLUMN]
        self.__game_board[row][column] = name

    def add_car(self, car):
        """
        Adds a car to the game.
        :param car: car object of car to add
        :return: True upon success. False if failed
        """
        # checks
        if car in self.__cars:
            return False
        car_name = car.get_name()
        car_coords = car.car_coordinates()
        for coordinate in car_coords:
            if not self.coord_ok(coordinate):
                return False
        # after passing all checks, add to board
        for coordinate in car_coords:
            self.fill_coord(coordinate, car_name)
        self.__cars.append(car)
        return True

    def move_car(self, name, movekey):
        """
        moves car one step in given direction.
        :param name: name of the car to move
        :param movekey: Key of move in car to activate
        :return: True upon success, False otherwise
        """
        req_car = None
        for car in self.__cars:
            if car.get_name() == name:
                req_car = car
        if req_car is None:
            return False
        move_coord = req_car.movement_requirements(movekey)[0]
        if not self.coord_ok(move_coord):
            return False
        moved = req_car.move(movekey)
        if not moved:
            return False
        self.fill_coord(move_coord, name)
        prev_coord = req_car.movement_requirements(Board.OPPOSITE_DIRECTION[movekey])[0]
        self.fill_coord(prev_coord, Board.EMPTY_CELL)
        return True
