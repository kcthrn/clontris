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


import logging

from clontris.core import Playfield


class Game():
    """The class coordinates all actions in Clontris."""

    def __init__(self):
        self._playfield = Playfield()
        self.rows = self._playfield.rows
        self.columns = self._playfield.columns

    def hard_drop(self):
        logging.debug("Game: Did hard drop")

    def rotate_acw(self):
        logging.debug("Game: Did anti-clockwise rotation")

    def rotate_cw(self):
        logging.debug("Game: Did clockwise rotation")

    def shift_left(self):
        logging.debug("Game: Did shift left")

    def shift_right(self):
        logging.debug("Game: Did shift right")

    def update(self):
        logging.debug("Game: Nothing to update :D")

    def get_cell_state(self, row, column):
        """Return the state of a cell in the Playfield.

        Rows and columns are counted from 0."""
        return self._playfield.get_cell_state(row, column)
