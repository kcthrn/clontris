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


"""This module containts project metadata.

If using setuptools, then within setup.py put::

   meta = {}
   with open(clontris/meta.py) as f:
       exec(f.read(), meta)

Then access this module's attributes like this::

   version = meta['version']
"""

package_name = 'clontris'
project_name = 'Clontris'
version = '0.1.0'
