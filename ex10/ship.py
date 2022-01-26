class Ship:
    """
    This is a class meant to represent ships
    """
    def __init__(self, x, y, speed_x, speed_y, heading,radius):
        """
        A constructor for a ship object
        :param x: location on the horizontal axis
        :param y: location on the vertical axis
        :param speed_x: speed on the horizontal axis
        :param speed_y: speed on the vertical axis
        :param heading: heading of the torpedo in degrees
        :param radius: radius of the ship
        """
        self.__x = x
        self.__y = y
        self.__speed_x = speed_x
        self.__speed_y = speed_y
        self.__heading = heading
        self.__radius=radius

    def get_x(self):
        """
        :return: Location on the horizontal axis
        """
        return self.__x

    def set_x(self, val):
        """
        This function changes the value of x into a chosen value
        :param val: New Location on the horizontal axis
        """
        self.__x = val

    def get_y(self):
        """
        :return: Location on the vertical axis
        """
        return self.__y

    def set_y(self, val):
        """
         This function changes the value of y into a chosen value
         :param val: New Location on the vertical axis
         """
        self.__y = val

    def get_speed_x(self):
        """
        :return: Speed of the ship on the horizontal axis
        """
        return self.__speed_x

    def set_speed_x(self, val):
        """
         This function changes the speed of the ship on the horizontal axis into a chosen value
         :param val: New speed of the ship on the horizontal axis
         """
        self.__speed_x = val

    def get_speed_y(self):
        """
        :return: Speed of the ship on the vertical axis
        """
        return self.__speed_y

    def set_speed_y(self, val):
        """
         This function changes the speed of the ship on the vertical axis into a chosen value
         :param val: New speed of the ship on the vertical axis
         """
        self.__speed_y = val

    def get_heading(self):
        """
        :return: Heading of the ship in degrees
        """
        return self.__heading

    def set_heading(self, val):
        """
         This function changes the heading of the ship in degrees into a chosen value
         :param val: New heading of the ship
         """
        self.__heading = val

    def get_radius(self):
        """
        :return: Radius of the ship
        """
        return self.__radius
