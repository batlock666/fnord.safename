# -*- coding: utf-8 -*-

# Copyright 2013, Bert Vanderbauwhede
#
# This file is part of fnord.safename.
#
# fnord.safename is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# fnord.safename is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public
# License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with fnord.safename.  If not, see <http://www.gnu.org/licenses/>.

import unittest


class SafenameCodecTestCase(unittest.TestCase):
    """Test-case for codec ``safename``.
    """

    def setUp(self):
        """Set up.
        """
        import fnord.safename

    def test_encode(self):
        """Test for the encoding.
        """
        self.assertEqual("spam".encode("safename"), "spam")
        self.assertEqual("Spam".encode("safename"), "{s}pam")
        self.assertEqual("SPAM".encode("safename"), "{spam}")
        self.assertEqual("spam eggs".encode("safename"), "spam_eggs")
        self.assertEqual("spam   eggs".encode("safename"), "spam___eggs")
        self.assertEqual(u"spàm".encode("safename"), "sp(e0)m")
