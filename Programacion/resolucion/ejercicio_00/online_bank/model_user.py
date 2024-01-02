import random, time

def gen_random_code(lenght):
    random.seed(time.time())
    digits = [random.randint(0, 9) for _ in range(lenght)]

    # Formar el código combinando los dígitos
    code = int(''.join(map(str, digits)))
    return code

class User():
    def __init__(self, name, paswd):
        self.name = name
        self.paswd = paswd
        self.user_code = gen_random_code(4)
        self.money = 0