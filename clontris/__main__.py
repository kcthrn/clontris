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


from kivy.config import Config
Config.set('kivy', 'log_level', 'debug')
# Restrict PlayfieldView's size
Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 240)
Config.set('graphics', 'height', 528)

from kivy.app import App
from kivy.clock import Clock
from kivy.logger import Logger

from clontris import meta
from clontris.game import Game
from clontris.view import PlayfieldView
from clontris.input import KeyboardHandler


class Clontris(App):

    def build(self):
        self.title = meta.project_name
        self.game = Game()
        self.root = PlayfieldView(self.game)
        KeyboardHandler(self.game)

        # TODO: Change framerate later to 1/30 or 1/60
        framerate = 1  # in seconds
        Clock.schedule_interval(self.game_loop, framerate)
        Logger.info("Clontris: Scheduled game loop")

    def game_loop(self, dt):
        self.game.update()
        self.root.draw()


if __name__ == '__main__':
    Clontris().run()
