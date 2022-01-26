class Asteroid:
    """
    This is a class meant to represent asteroids
    """
    def __init__(self, x, y, speed_x, speed_y, size,radius):
        """
        A constructor for an asteroid object
        :param x: location on the horizontal axis
        :param y: location on the vertical axis
        :param speed_x: speed on the horizontal axis
        :param speed_y: speed on the vertical axis
        :param size: size of the Asteroid
        :param radius: radius of the Asteroid
        """
        self.__x = x
        self.__y = y
        self.__speed_x = speed_x
        self.__speed_y = speed_y
        self.__size = size
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
        :return: Speed of the asteroid on the horizontal axis
        """
        return self.__speed_x

    def get_speed_y(self):
        """
        :return: Speed of the asteroid on the vertical axis
        """
        return self.__speed_y

    def get_size(self):
        """
        :return: Size of the asteroid
        """
        return self.__size

    def get_radius(self):
        """
        :return: Radius of the asteroid
        """
        return self.__radius

    def has_intersection(self, obj):
        """
        This function checks if the asteroid has an intersection with another object
        :param obj: another object
        :return: True if there is an intersection, else, False
        """
        obj_x = obj.get_x()
        obj_y = obj.get_y()
        distance = ((obj_x - self.__x) ** 2 + (obj_y - self.__y) ** 2) ** 0.5
        return distance <= self.get_radius() + obj.get_radius()
