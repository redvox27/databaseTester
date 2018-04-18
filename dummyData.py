import string
import random

class DummyDataGenerator:

    def __init__(self):
        self.letter_list = [i for i in string.ascii_lowercase[:26]]

    def get_list(self):
        return self.letter_list

    def generate_random_string(self, number_of_characters):
        rand_string = ''
        for i in range(0, number_of_characters):
            rand_int = random.randint(0, 25)
            character = self.get_list()[rand_int]
            rand_string += character

        return rand_string

