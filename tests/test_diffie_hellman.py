import unittest

from crypto.diffie_hellman import DiffieHellman


class TestDiffieHellman(unittest.TestCase):
    def test_correct(self):
        prime_dividers = [
            3,
            98764321261
        ]
        
        generators = [
            1,
            2,
            3,
            17,
            98764321261
        ]

        for p in prime_dividers:
            for g in generators:
                alice = DiffieHellman(g, p)
                bob = DiffieHellman(g, p)
                A = alice.public_key
                B = bob.public_key
                self.assertEqual(
                    alice.make_secret(B), bob.make_secret(A))

    def test_prime_divider_gross_than_two(self):
        with self.assertRaises(ValueError):
            DiffieHellman(3, 1)
            DiffieHellman(3, 2)


__all__ = ['TestDiffieHellman']