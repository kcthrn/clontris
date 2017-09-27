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


"""This module contains custom widget definitions."""

from kivy.graphics import Color, Rectangle
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.logger import Logger


class CellView(Widget):
    """This is a visual representation of a cell in the Playfield.

    A cell is black when "empty" and white when "occupied" by a square.
    """

    def __init__(self, row, column, **kwargs):
        super().__init__(**kwargs)
        # A cell is identified by its row and column values
        # This widget will represent only that cell
        self.row = row
        self.column = column
        with self.canvas:
            self.canvas.clear()
            self.color = Color(a=0)
            self.rect = Rectangle(pos=self.pos, size=self.size)

    def draw(self):
        """Change colour to reflect a cell's state."""
        cell_state = self.parent.game.get_cell_state(self.row, self.column)
        if cell_state == 0:
            self.color.rgba = (0, 0, 0, 1)
        else:
            self.color.rgba = (1, 1, 1, 1)
        self.rect.pos = self.pos
        self.rect.size = self.size


class PlayfieldView(GridLayout):
    # TODO: Document PlayfieldView
    """This is a view into the game's Playfield.

    Rows and columns are counted from 0.
    """
    def __init__(self, game, **kwargs):
        super().__init__(**kwargs)
        self.game = game
        self.cols = game.columns  # need for Layout
        self.spacing = ['1dp']
        # Need to place children from the top row toward the bottom
        for row in range(game.rows-1, -1, -1):
            for column in range(game.columns):
                self.add_widget(CellView(row, column))
        Logger.debug("PlayfieldView: Initialized")

    def draw(self):
        """Update each CellView's canvas to reflect cell states."""
        for cell in self.walk(restrict=True):
            if cell != self:
                cell.draw()
