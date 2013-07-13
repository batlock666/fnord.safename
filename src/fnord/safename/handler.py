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
