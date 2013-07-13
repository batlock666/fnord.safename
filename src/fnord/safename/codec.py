import codecs

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


def safename_encode(string, errors="strict"):
    """Encode a string with codec ``safename``.
    """
    if errors != "strict":
        raise UnicodeError(u"Unsupported error handling: %s" % errors)

    try:
        return _safename_encode_chain(string), len(string)
    except UnicodeError as error:
        raise UnicodeEncodeError(error.args[0])


def safename_decode(string, errors="strict"):
    """Decode a string with codec ``safename``.
    """
    if errors != "strict":
        raise UnicodeError(u"Unsupported error handling: %s" % errors)

    try:
        return _safename_decode_chain(string), len(string)
    except UnicodeError as error:
        raise UnicodeDecodeError(error.args[0])


class SafenameCodec(codecs.Codec):
    """Codec ``safename``.
    """

    def encode(self, string, errors="strict"):
        """Encode a string with codec ``safename``.
        """
        return safename_encode(string, errors=errors)

    def decode(self, string, errors="strict"):
        """Decode a string with codec ``safename``.
        """
        return safename_decode(string, errors=errors)
