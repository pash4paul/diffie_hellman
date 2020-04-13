import random


class DiffieHellman:
    def __init__(self, generator, prime_divider):
        if prime_divider <= 2:
            raise ValueError('prime_divider must be gross than 2')
        self.__prime_divider = prime_divider
        self.__private_key = random.randint(2, prime_divider - 1)
        self.__public_key = pow(
            generator, self.__private_key, prime_divider
        )

    @property
    def public_key(self):
        return self.__public_key


    def make_secret(self, B):
        return pow(B, self.__private_key, self.__prime_divider)