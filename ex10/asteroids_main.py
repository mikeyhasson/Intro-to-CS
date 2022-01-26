#################################################################
# FILE : asteroids_main.py
# WRITER : Michael Hasson , mikey641 , 322893892
# EXERCISE : intro2cs2 ex10 2020
# DESCRIPTION: Asteroids game
#################################################################
from screen import Screen
from ship import Ship
from asteroid import Asteroid
from torpedo import Torpedo
import random
from math import cos, sin, radians
import sys

DEFAULT_ASTEROIDS_NUM = 5
INITIAL_ASTEROID_SIZE = 3
MIN_ASTEROID_SPEED = 1
MAX_ASTEROID_SPEED = 4
SMALLEST_ASTEROID_SIZE = 1
ASTEROID_DIVIDE_AMOUNT = 2

DEF_SHIP_SPEED = 0
DEF_HEADING = 0
DEF_HP = 3

SHIP_RADIUS = 1
TORPEDO_RADIUS = 4

SIZE_THREE_SCORE = 20
SIZE_TWO_SCORE = 50
SIZE_ONE_SCORE = 100
SCORES = {1: SIZE_ONE_SCORE, 2: SIZE_TWO_SCORE, 3: SIZE_THREE_SCORE}

MAX_TORPEDOS_AMOUNT = 10
MAX_TORPEDO_LIFESPAN = 200

SHIP_COLLISION_TITLE, SHIP_COLLISION_MESSAGE = "Collision", "Your ship has hit an asteroid, you lose 1 life"
NO_ASTEROIDS_TITLE, NO_ASTEROIDS_MESSAGE = "You won", "You destroyed all the asteroids, we hope you've enjoyed the game"
NO_HP_TITLE, NO_HP_MESSAGE = "You lost", "Your ship has taken too much damage. Better luck next time"
SHOULD_EXIT_TITLE, SHOULD_EXIT_MESSAGE = "Exiting game", "Game is over as requested"


class GameRunner:
    """
    This is a class that represents the asteroids game.
    """

    def __init__(self, asteroids_amount):
        """
        A constructor for a GameRunner object
        :param asteroids_amount: initial amount of asteroids
        """
        self.__screen = Screen()

        self.__screen_max_x = Screen.SCREEN_MAX_X
        self.__screen_max_y = Screen.SCREEN_MAX_Y
        self.__screen_min_x = Screen.SCREEN_MIN_X
        self.__screen_min_y = Screen.SCREEN_MIN_Y
        # creating ship object
        ship_x, ship_y = self.random_coords()
        self.__ship = Ship(ship_x, ship_y, DEF_SHIP_SPEED, DEF_SHIP_SPEED, DEF_HEADING, SHIP_RADIUS)
        self.__hp = DEF_HP
        # creating torpedo and asteroid lists and setting user score to 0.
        self.__score = 0
        self.__torpedos = []
        self.__asteroids = []

        # creating asteroids and adding them to the list and screen
        for i in range(asteroids_amount):
            x, y = ship_x, ship_y
            while x == ship_x and y == ship_y:
                x, y = self.random_coords()
            speed_x, speed_y = self.random_speed(), self.random_speed()
            size = INITIAL_ASTEROID_SIZE
            radius = self.calculate_asteroid_radius(size)
            new_asteroid = Asteroid(x, y, speed_x, speed_y, size, radius)
            self.__asteroids.append(new_asteroid)
            self.__screen.register_asteroid(new_asteroid, size)

    def calculate_asteroid_radius(self, size):
        """
        This function calculates an asteroid's radius according to its' size
        :param size: size of the asteroid
        :return: radius of the asteroid
        """
        return size * 10 - 5

    def random_speed(self):
        """
        :return: random  integer speed between |1|<=v<=4
        """
        speed = random.randint(MIN_ASTEROID_SPEED, MAX_ASTEROID_SPEED)
        sign = random.choice([-1, 1])
        return sign * speed

    def random_coords(self):
        """
        :return: random integer coorinates in the form of x,y, the are within the screen's bounds.
        """
        x = random.randint(self.__screen_min_x, self.__screen_max_x)
        y = random.randint(self.__screen_min_y, self.__screen_max_y)
        return x, y

    def move_object(self, obj):
        """
        This function moves a single object according to a given formula
        :param obj:Ship,Torpedo or Asteroid object
        """
        x = obj.get_x()
        y = obj.get_y()
        speed_x = obj.get_speed_x()
        speed_y = obj.get_speed_y()
        new_x = self.__screen_min_x + (x + speed_x - self.__screen_min_x) % (self.__screen_max_x - self.__screen_min_x)
        new_y = self.__screen_min_y + (y + speed_y - self.__screen_min_y) % (self.__screen_max_y - self.__screen_min_y)
        obj.set_x(new_x)
        obj.set_y(new_y)

    def move(self):
        """
        This function uses the function move_object to move the ship, asteroids and torpedos on the screen
        """
        self.move_object(self.__ship)
        for asteroid in self.__asteroids:
            self.move_object(asteroid)
        for torpedo in self.__torpedos:
            self.move_object(torpedo)

    def draw(self):
        """
        This function draws the objects of the game on the screen using Class screen
        """
        self.__screen.draw_ship(self.__ship.get_x(), self.__ship.get_y(), self.__ship.get_heading())
        for asteroid in self.__asteroids:
            self.__screen.draw_asteroid(asteroid, asteroid.get_x(), asteroid.get_y())
        for torpedo in self.__torpedos:
            self.__screen.draw_torpedo(torpedo, torpedo.get_x(), torpedo.get_y(), torpedo.get_heading())

    def rotate_ship(self):
        """
        This function checks if the left or right keys were pressed on the keyboard and rotates the ship according
        to what key was pressed
        """
        if self.__screen.is_left_pressed():
            self.__ship.set_heading(self.__ship.get_heading() + 7)
        if self.__screen.is_right_pressed():
            self.__ship.set_heading(self.__ship.get_heading() - 7)

    def accelerate_ship(self):
        """
        This function checks if the up key was pressed and accelerates the ship in its' direction
        """
        if self.__screen.is_up_pressed():
            heading = self.__ship.get_heading()
            speed_x = self.__ship.get_speed_x()
            self.__ship.set_speed_x(speed_x + cos(radians(heading)))
            speed_y = self.__ship.get_speed_y()
            self.__ship.set_speed_y(speed_y + sin(radians(heading)))

    def collision(self):
        """
        This function checks if any ship or torpedo objects hit an asteroid.
        """
        for asteroid in self.__asteroids:
            # if asteroid hit a ship
            if asteroid.has_intersection(self.__ship):
                self.__hp -= 1
                self.__screen.remove_life()
                self.__screen.show_message(SHIP_COLLISION_TITLE, SHIP_COLLISION_MESSAGE)
                self.__asteroids.remove(asteroid)
                self.__screen.unregister_asteroid(asteroid)
                return  # preventing shooting a torpedo when hit by asteroid
            # if asteroid hit a torpedo
            for torpedo in self.__torpedos:
                if asteroid.has_intersection(torpedo):
                    self.asteroid_torpedo_collision(asteroid, torpedo)

    def asteroid_torpedo_collision(self, asteroid, torpedo):
        """
        This function is called when a torpedo has collided into an asteroid. It changes the score and removes the hit
        objects.
        :param asteroid: an Asteroid object
        :param torpedo: A Torpedo object
        """
        # adding ascore
        asteroid_size = asteroid.get_size()
        self.__score += SCORES[asteroid_size]
        self.__screen.set_score(self.__score)
        # if asteroid size was bigger than 1, divide it into 2 smaller asteroids
        if asteroid_size != SMALLEST_ASTEROID_SIZE:
            for i in range(ASTEROID_DIVIDE_AMOUNT):
                org_speed_x = asteroid.get_speed_x()
                org_speed_y = asteroid.get_speed_y()
                speed_x = ((-1) ** i) * (torpedo.get_speed_x() + org_speed_x) / (
                            org_speed_x ** 2 + org_speed_y ** 2) ** 0.5
                speed_y = ((-1) ** i) * (torpedo.get_speed_y() + org_speed_y) / (
                            org_speed_x ** 2 + org_speed_y ** 2) ** 0.5
                new_size = asteroid_size - 1
                new = Asteroid(asteroid.get_x(), asteroid.get_y(), speed_x, speed_y,
                               new_size, self.calculate_asteroid_radius(new_size))
                self.__asteroids.append(new)
                self.__screen.register_asteroid(new, new_size)
        # removing asteroid and torpedo from lists and screen
        self.__asteroids.remove(asteroid)
        self.__screen.unregister_asteroid(asteroid)
        self.__torpedos.remove(torpedo)
        self.__screen.unregister_torpedo(torpedo)

    def shoot_torpedo(self):
        """
        This function checks if the space key was pressed, if so, it will check that there aren't too many torpedos
        on the screen and shoot a new torpedo
        """
        if self.__screen.is_space_pressed() and len(self.__torpedos) < MAX_TORPEDOS_AMOUNT:
            x, y = self.__ship.get_x(), self.__ship.get_y()
            speed_x = self.__ship.get_speed_x() + 2 * cos(radians(self.__ship.get_heading()))
            speed_y = self.__ship.get_speed_y() + 2 * sin(radians(self.__ship.get_heading()))
            heading = self.__ship.get_heading()
            torpedo = Torpedo(x, y, speed_x, speed_y, heading, TORPEDO_RADIUS)
            self.__torpedos.append(torpedo)
            self.__screen.register_torpedo(torpedo)

    def update_torpedos_lifespan(self):
        """
        This function updates the lifespan of the torpedos on the screen and removes the ones who have exceeded their
        lifespan
        """
        for torpedo in self.__torpedos:
            torpedo.add_one_lifespan()
            if torpedo.get_lifespan() > MAX_TORPEDO_LIFESPAN:
                self.__torpedos.remove(torpedo)
                self.__screen.unregister_torpedo(torpedo)

    def exit(self):
        """
        This function checks if the game should end at every interation. If so, it will end it.
        """
        exit_game = False
        if len(self.__asteroids) == 0:
            self.__screen.show_message(NO_ASTEROIDS_TITLE, NO_ASTEROIDS_MESSAGE)
            exit_game = True
        elif self.__hp == 0:
            self.__screen.show_message(NO_HP_TITLE, NO_HP_MESSAGE)
            exit_game = True
        elif self.__screen.should_end():
            self.__screen.show_message(SHOULD_EXIT_TITLE, SHOULD_EXIT_MESSAGE)
            exit_game = True
        if exit_game:
            self.__screen.end_game()
            sys.exit()

    def run(self):
        self._do_loop()
        self.__screen.start_screen()

    def _do_loop(self):
        # You should not to change this method!
        self._game_loop()
        # Set the timer to go off again
        self.__screen.update()
        self.__screen.ontimer(self._do_loop, 5)

    def _game_loop(self):
        """
        This function is repeated until the game is over. It calls the other functions in the class and builds the game.
        """
        self.draw()
        self.move()
        self.rotate_ship()
        self.accelerate_ship()
        self.collision()
        self.shoot_torpedo()
        self.update_torpedos_lifespan()
        self.exit()

def main(amount):
    runner = GameRunner(amount)
    runner.run()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(DEFAULT_ASTEROIDS_NUM)
