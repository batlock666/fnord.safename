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


def safename_encode(string, errors="strict"):
    """Encode a string with codec ``safename``.
    """
    if errors != "strict":
        raise UnicodeError(u"Unsupported error handling: %s" % errors)

    try:
        return _safename_encode_chain(string), len(string)
    except UnicodeError as error:
        raise UnicodeEncodeError(error.args[0])
