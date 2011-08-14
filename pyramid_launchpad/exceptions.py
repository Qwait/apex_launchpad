class MessageException(Exception):
    def __init__(self, message=None):
        Exception.__init__(self, message or self.message)