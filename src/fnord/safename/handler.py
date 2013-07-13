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
