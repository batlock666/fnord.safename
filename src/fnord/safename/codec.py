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

import codecs
import re

from fnord.easycodec import encoder, decoder
from fnord.easycodec import CodecSearch, AUTO

ENCODE_SCANNER = re.Scanner([
    (r"[A-Z]+", lambda scanner, token: "{%s}" % token.lower()),
    (r" +", lambda scanner, token: token.replace(" ", "_")),
    (r"[a-z0-9\-+!$%&'@~#.,^]+", lambda scanner, token: token),
    (r".", lambda scanner, token: "(%s)" % hex(ord(token))[2:])])
DECODE_SCANNER = re.Scanner([
    (r"\{[a-z]+\}", lambda scanner, token: token[1:-1].upper()),
    (r"_+", lambda scanner, token: token.replace("_", " ")),
    (r"[a-z0-9\-+!$%&'@~#.,^]+", lambda scanner, token: token),
    (r"\([0-9a-f]+\)", lambda scanner, token: unichr(int(token[1:-1], 16)))])


@encoder("safename")
def safename_encode(string):
    """Encoder for codec ``safename``.
    """
    scanned = ENCODE_SCANNER.scan(string)
    if scanned[1]:
        raise UnicodeEncodeError(
            "safename", u"", 0, len(string), "Can't encode string"
        )
    return u"".join(scanned[0])


@decoder("safename")
def safename_decode(string):
    """Decoder for codec ``safename``.
    """
    scanned = DECODE_SCANNER.scan(string)
    if scanned[1]:
        raise UnicodeDecodeError(
            "safename", "", 0, len(string), "Can't decode string"
        )
    return u"".join(scanned[0])

codecs.register(CodecSearch(
    "safename", safename_encode, safename_decode,
    incrementalencoder=AUTO, incrementaldecoder=AUTO,
    streamwriter=AUTO, streamreader=AUTO))
