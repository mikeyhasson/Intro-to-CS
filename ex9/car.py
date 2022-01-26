class Car:
    """
    This is a class meant to represent cars
    """
    ROW,COLUMN=0,1
    VERTICAL,HORIZONTAL=0,1
    UP,DOWN,LEFT,RIGHT='u','d','l','r'
    LAST_COORD=-1

    def __init__(self, name, length, location, orientation):
        """
        A constructor for a Car object
        :param length: A positive int representing the car's length.
        :param location: A tuple representing the car's head (row, col) location
        :param orientation: One of either 0 (VERTICAL) or 1 (HORIZONTAL)
        """
        self.__name=name
        self.__length=length
        self.__location=location
        self.__orientation=orientation

    def car_coordinates(self):
        """
        :return: A list of coordinates the car is in
        """
        coords=[]
        org_row=self.__location[Car.ROW]
        org_column=self.__location[Car.COLUMN]
        for i in range(self.__length):
            if self.__orientation==Car.ROW:
                new_coord=(org_row + i,org_column)
            else:
                new_coord=(org_row,org_column + i)
            coords.append(new_coord)
        return coords

    def possible_moves(self):
        """
        :return: A dictionary of strings describing possible movements permitted by this car.
        """

        if self.__orientation==Car.VERTICAL:
            return {Car.UP:"cause the car to move up",Car.DOWN:"cause the car to move down"}
        else:
            return {Car.LEFT:"cause the car to move left",Car.RIGHT:"cause the car to move right"}

    def movement_requirements(self, movekey):
        """ 
        :param movekey: A string representing the key of the required move.
        :return: A list of cell locations which must be empty in order for this move to be legal.
        """
        new_row = self.__location[Car.ROW]
        new_column = self.__location[Car.COLUMN]
        if movekey == Car.UP:
            new_row = self.__location[Car.ROW] - 1
        elif movekey == Car.DOWN:
            new_row = self.car_coordinates()[Car.LAST_COORD][Car.ROW] + 1
        elif movekey == Car.LEFT:
            new_column = self.__location[Car.COLUMN] - 1
        elif movekey == Car.RIGHT:
            new_column = self.car_coordinates()[Car.LAST_COORD][Car.COLUMN] + 1
        return [(new_row,new_column)]

    def move(self, movekey):
            """
            :param movekey: A string representing the key of the required move.
            :return: True upon success, False otherwise
            """
            if not movekey in self.possible_moves().keys():
                return False

            new_row = self.__location[Car.ROW]
            new_column = self.__location[Car.COLUMN]
            if movekey == Car.RIGHT:
                new_column+=1
            elif movekey == Car.LEFT:
                new_column-=1
            elif movekey == Car.DOWN:
                new_row+=1
            elif movekey == Car.UP:
                new_row-=1
            self.__location = (new_row, new_column)
            return True

    def get_name(self):
            """
            :return: The name of this car.
            """
            return self.__name
