# Copyright (C) 2017 Kacy Thorne
#
# This file is part of Clontris.
#
# Clontris is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Clontris is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


"""This module contains input handlers."""

from kivy.core.window import Window


class KeyboardHandler():
    """Forward player's actions processed from keyboard input to a Game
    controller object instance.

    .. note:: No simultaneous key presses
    """

    def __init__(self, game):
        self._game = game
        self._keyboard = Window.request_keyboard(None, self)
        self._keyboard.bind(on_key_down=self._on_key_down)

    def _on_key_down(self, keyboard, keycode, *args):
        if keycode[1] == 'left':
            self._game.shift_left()

        elif keycode[1] == 'right':
            self._game.shift_right()

        elif keycode[1] == 'z':
            self._game.rotate_acw()

        elif keycode[1] == 'x':
            self._game.rotate_cw()

        elif keycode[1] == 'spacebar':
            self._game.hard_drop()
