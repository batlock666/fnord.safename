# -*- coding: utf-8 -*-

import optparse
import os
import os.path


def safename():
    """Script to rename files using codec ``safename``.
    """
    parser = optparse.OptionParser()
    parser.add_option(
        "-e",
        "--encode",
        action="store_const",
        dest="action",
        const="encode",
        help="Encode filenames",
    )
    parser.add_option(
        "-d",
        "--decode",
        action="store_const",
        dest="action",
        const="decode",
        help="Decode filenames",
    )
    parser.add_option(
        "-t",
        "--test",
        action="store_true",
        dest="test",
        default=False,
        help="Don't rename files",
    )
    parser.add_option(
        "-v",
        "--verbose",
        action="store_true",
        dest="verbose",
        help="Show more information",
    )

    options, paths = parser.parse_args()
    for path in paths:
        path = path.decode("utf-8")
        path = os.path.normpath(path)
        directory, filename = os.path.split(path)

        if options.action == "encode":
            try:
                new = os.path.join(directory, filename.encode("safename"))
            except UnicodeEncodeError:
                print u"can't rename \"%s\"" % path
                continue
        elif options.action == "decode":
            try:
                new = os.path.join(directory, filename.decode("safename"))
            except UnicodeDecodeError:
                print u"can't rename \"%s\"" % path
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
