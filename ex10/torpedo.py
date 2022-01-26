class Torpedo:
    """
    This is a class meant to represent torpedos
    """
    def __init__(self, x, y, speed_x, speed_y, heading,radius):
        """
        A constructor for a torpedo object
        :param x: location on the horizontal axis
        :param y: location on the vertical axis
        :param speed_x: speed on the horizontal axis
        :param speed_y: speed on the vertical axis
        :param heading: heading of the torpedo in degrees
        :param radius: radius of the torpedo
        """
        self.__x = x
        self.__y = y
        self.__speed_x = speed_x
        self.__speed_y = speed_y
        self.__heading = heading
        self.__radius=radius
        self.__lifespan=0

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
        :return: Speed of the torpedo on the horizontal axis
        """
        return self.__speed_x

    def get_speed_y(self):
        """
        :return: Speed of the torpedo on the vertical axis
        """
        return self.__speed_y

    def get_heading(self):
        """
        :return: Heading of the torpedo in degrees
        """
        return self.__heading

    def get_radius(self):
        """
        :return: Radius of the torpedo
        """
        return self.__radius

    def add_one_lifespan(self):
        """
        This function changes the value of the torpedo's value by 1
        """
        self.__lifespan+=1

    def get_lifespan(self):
        """
        :return: Lifespan of the torpedo
        """
        return self.__lifespan
