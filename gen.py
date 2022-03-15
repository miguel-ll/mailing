import string
import random
def gen_user():
    ram = string.ascii_uppercase + string.ascii_lowercase + string.digits
    numb = random.randint(8, 14)
    for i in range(numb):
        return "".join(random.sample(ram, numb))
        
def gen_pass():
    ram = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    numb = random.randint(7, 10)
    for i in range(numb):
        return "".join(random.sample(ram, numb))
