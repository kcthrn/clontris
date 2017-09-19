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

from kivy.uix.widget import Widget
from kivy.logger import Logger


class View(Widget):
    """This is a view into the game."""

    def draw(self):
        """update the canvas."""
        Logger.debug("View: Nothing to draw :(")
