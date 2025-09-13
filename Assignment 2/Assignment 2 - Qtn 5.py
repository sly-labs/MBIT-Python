# an example demonstrating how to use Abstract Base Classes (ABC) in Python to define a contract for file handlers.
# This ensures that any concrete class (like TextFileHandler or BinaryFileHandler) must implement the required read() and write() methods.
from abc import ABC, abstractmethod


# Define the abstract base class
class FileHandler(ABC):
    """Abstract base class for all file handlers."""

    @abstractmethod
    def read(self):
        """Read data from the file."""
        pass

    @abstractmethod
    def write(self, data):
        """Write data to the file."""
        pass


# Concrete implementation for handling text files
class TextFileHandler(FileHandler):
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, 'r', encoding='utf-8') as file:
            return file.read()

    def write(self, data):
        with open(self.filename, 'w', encoding='utf-8') as file:
            file.write(data)
        print(f"Text data written to {self.filename}")


# Concrete implementation for handling binary files
class BinaryFileHandler(FileHandler):
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        with open(self.filename, 'rb') as file:
            return file.read()

    def write(self, data):
        with open(self.filename, 'wb') as file:
            file.write(data)
        print(f"Binary data written to {self.filename}")


# Example usage
if __name__ == "__main__":
    # Text file handling
    text_handler = TextFileHandler("example.txt")
    text_handler.write("Hello, this is a text file.")
    content = text_handler.read()
    print("Text File Content:", content)

    # Binary file handling
    binary_handler = BinaryFileHandler("example.bin")
    binary_data = bytes([10, 20, 30, 40, 50])
    binary_handler.write(binary_data)
    data = binary_handler.read()
    print("Binary File Data:", list(data))

"""
Key Points:
ABC and @abstractmethod: These ensure that FileHandler cannot be instantiated directly, and any subclass must implement read() and write() methods.
Enforced Interface: If you try to create a subclass without implementing these methods, Python will raise an error when you try to instantiate it.
"""