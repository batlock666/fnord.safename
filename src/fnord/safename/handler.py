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

import re


class Handler(object):
    """String-handler.
    """

    def __init__(self, regexp, handle):
        """Constructor.
        """
        self.regexp = re.compile("(?P<head>%s)(?P<tail>.*)" % regexp)
        self.handle = handle

    def __call__(self, string):
        """Callable.
        """
        match = self.regexp.match(string)
        if match is None:
            return "", string
        else:
            head = self.handle(match.group("head"))
            tail = match.group("tail")
            return head, tail


class HandlerChain(object):
    """Chain of string-handlers.
    """

    def __init__(self, *args):
        """Constructor.
        """
        self.handlers = list(args)

    def __call__(self, string):
        """Callable.
        """
        result = ""
        while (string):
            for handler in self.handlers:
                head, tail = handler(string)
                if head:
                    result += head
                    string = tail
                    break
            else:
                raise UnicodeError(u"Can't handle string: %s" % string)

        return result
