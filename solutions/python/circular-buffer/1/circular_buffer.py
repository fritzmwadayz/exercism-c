class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message


class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity 
        self.read_index = 0
        self.write_index = 0
        self.count = 0

    def read(self):
        if self.count == 0:
            raise BufferEmptyException("Circular buffer is empty")
        data = self.buffer[self.read_index]
        self.buffer[self.read_index] = None
        self.read_index = (self.read_index+1) % self.capacity
        self.count -= 1
        return data        

    def write(self, data):
        if self.count == self.capacity:
            raise BufferFullException("Circular buffer is full")
        self.buffer[self.write_index] = data
        self.write_index = (self.write_index + 1) % self.capacity
        self.count += 1
    
    def overwrite(self, data):
        if self.count == self.capacity:
            self.buffer[self.read_index] = data
            self.read_index = (self.read_index + 1) % self.capacity
            self.write_index = (self.write_index + 1) % self.capacity
        else:
            self.buffer[self.write_index] = data
            self.write_index = (self.write_index + 1) % self.capacity
            self.count += 1
            
    def clear(self):
        self.buffer = [None] * self.capacity
        self.read_index = 0
        self.write_index = 0
        self.count = 0
