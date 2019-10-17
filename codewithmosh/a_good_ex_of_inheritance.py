class InvalidOperationError(Exception):
    pass


class Stream:
    def __index__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError('Stream is already opened')
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError('Stream is already closed')
        self.opened = False


class FileStream(Stream):
    def read(self):
        print('Rading data from the file')


class NetworkStream(Stream):
    def read(self):
        print('Rading data from the network')
        ƒƒ