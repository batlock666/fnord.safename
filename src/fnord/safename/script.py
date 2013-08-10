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

import optparse
import os
import os.path


def _expand_paths(recursive, paths):
    """Expand all the paths, if necessary.
    """
    for path in paths:
        if recursive and os.path.isdir(path):
            for (dirpath, dirnames, filenames) in os.walk(path, topdown=False):
                for dirname in dirnames:
                    yield os.path.join(dirpath, dirname)
                for filename in filenames:
                    yield os.path.join(dirpath, filename)
        yield path


def safename():
    """Script to rename files using codec ``safename``.
    """
    parser = optparse.OptionParser()
    parser.add_option(
        "-d",
        "--decode",
        action="store_const",
        dest="action",
        const="decode",
        help="decode from safe filenames for the given files",
    )
    parser.add_option(
        "-e",
        "--encode",
        action="store_const",
        dest="action",
        const="encode",
        help="encode to safe filenames for the given files",
    )
    parser.add_option(
        "-r",
        "--recursive",
        action="store_true",
        dest="recursive",
        default=False,
        help="decode or encode filenames recursively",
    )
    parser.add_option(
        "-t",
        "--test",
        action="store_true",
        dest="test",
        default=False,
        help="don't rename the files",
    )
    parser.add_option(
        "-v",
        "--verbose",
        action="store_true",
        dest="verbose",
        default=False,
        help="print out every renaming operation",
    )

    options, paths = parser.parse_args()
    for path in _expand_paths(options.recursive, paths):
        path = path.decode("utf-8")
        path = os.path.normpath(path)
        directory, filename = os.path.split(path)

        if options.action == "encode":
            try:
                new = os.path.join(directory, filename.encode("safename"))
            except UnicodeEncodeError:
                print u"can't encode \"%s\"" % path
                continue
        elif options.action == "decode":
            try:
                new = os.path.join(directory, filename.decode("safename"))
            except UnicodeDecodeError:
                print u"can't decode \"%s\"" % path
                continue
        else:
            print u"action is missing"
            return

        if path == new:
            continue

        if not options.test:
            try:
                os.rename(path, new)
            except OSError:
                print u"can't rename \"%s\"" % path
                continue

        if options.verbose:
            print u"renaming \"%s\" to \"%s\"" % (path, new)
