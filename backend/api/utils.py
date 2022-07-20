import random
import string

def get_random_string():
    result_str = ''.join(random.choice(string.ascii_letters) for i in range(6))
    n_string1 = str(random.randrange(10, 99))
    n_string2 = str(random.randrange(10, 99))
    result_str = n_string1 + result_str + n_string2

    return result_str

CONSTRANT_URL = '192.168.2.46:8000'