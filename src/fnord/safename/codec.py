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

from fnord.easycodec import encoder, decoder
from fnord.easycodec import CodecSearch, AUTO

from fnord.safename.handler import Handler, HandlerChain


_safename_encode_chain = HandlerChain(
    Handler(
        "[A-Z]+",
        lambda string: "{%s}" % string.lower()),
    Handler(
        " +",
        lambda string: string.replace(" ", "_")),
    Handler(
        "[a-z0-9\-+!$%&'@~#.,^]+",
        lambda string: string),
    Handler(
        ".",
        lambda string: "(%s)" % hex(ord(string))[2:]),
)

_safename_decode_chain = HandlerChain(
    Handler(
        "\{[a-z]+\}",
        lambda string: string[1:-1].upper()),
    Handler(
        "_+",
        lambda string: string.replace("_", " ")),
    Handler(
        "[a-z0-9\-+!$%&'@~#.,^]+",
        lambda string: string),
    Handler(
        "\([0-9a-f]+\)",
        lambda string: unichr(int(string[1:-1], 16))),
)


@encoder("safename")
def safename_encode(string):
    """Encoder for codec ``safename``.
    """
    return _safename_encode_chain(string)


@decoder("safename")
def safename_decode(string):
    """Decoder for codec ``safename``.
    """
    return _safename_decode_chain(string)

codecs.register(CodecSearch(
    "safename", safename_encode, safename_decode,
    incrementalencoder=AUTO, incrementaldecoder=AUTO,
    streamwriter=AUTO, streamreader=AUTO))
