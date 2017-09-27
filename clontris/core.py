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


"""This module contains the core functionality of the game."""


class Playfield():
    # TODO: Document Playfield

    def __init__(self):
        self._rows = 22
        self._columns = 10
        self._matrix = [
            [0 for column in range(self._columns)] for row in range(self._rows)
        ]

    @property
    def rows(self):
        """The total number of rows in the Playfield."""
        return self._rows

    @property
    def columns(self):
        """The total number of columns in the Playfield."""
        return self._columns

    def get_cell_state(self, row, column):
        # TODO: Document get_cell_state
        """Return the state of a cell.

        The state represents the presence of a square at that cell in the
        Playfield.

        Possible states:

        - 0 : The cell is empty
        - 1 : The cell is occupied
        """
        return self._matrix[row][column]
