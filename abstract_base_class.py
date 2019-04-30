from abc import ABC, abstractmethod

class InvalidOperationError(Exception):
    pass


class Stream(ABC):
    def __index__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError('stream already opened')
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError('stream already closed')
        self.opened = False

    @abstractmethod
    def read(self):
        self.open()
        print('stream reading the content')

class FileStream(Stream):
    def read(self):
        print('reading content from file')


class MemoryStream(Stream):
    def read(self):
        print('reading content from memory')


class NetworkStream(Stream):
    def read(self):
        print('reading content from network')


stream = NetworkStream()
stream.open()