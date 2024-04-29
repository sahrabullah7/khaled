# Import the 'unittest' module
import unittest

# Import the functions to be tested from the code
from codes import char_to_baudot, baudot_to_char, encrypt_phrase, decrypt_phrase

# Define a test class for the unittest
class TestBaudotEncryption(unittest.TestCase):
    # test the first function
    def test_char_to_baudot(self):
        # Test individual character to Baudot code conversion
        self.assertEqual(char_to_baudot('A'), '00011')
        self.assertEqual(char_to_baudot(' '), '00000')
        self.assertEqual(char_to_baudot('1'), '')  # Invalid characters