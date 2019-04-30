class InvalidOperationError(Exception):
    pass


class Stream:
    def __init__(self):
        self.opened = False

    def open(self):
        print('opened stream')
        self.opened = True

    def close(self):
        print('closed stream')
        self.opened = False

    def read(self):
        print('reading content')

    def read(self, locked):
        if locked:
            raise InvalidOperationError('Stream locked already')
        print('acquired lock and reading content')


class FileStream(Stream):
    def read(self):
        print('reading content from file')

    def read(self, locked):
        if locked:
            print('stream locked.. waiting to acquire one')
        else:
            print('acquired lock and reading content')


stream = FileStream()
stream.read(True)
stream.read()
ƒFƒ