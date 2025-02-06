"""
Solitaire clone.
"""

import arcade
import game


def main():
    """ Main function """
    window = game.MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
