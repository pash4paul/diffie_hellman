import unittest

from crypto.xor_cipher import encrypt, decrypt


class TestEncryption(unittest.TestCase):
    def test_correct_work(self):
        keys = [
            '1',
            '777',
            '-777',
            '-1',
            'a',
            'Hello',
            'h6RTe22oneOlZPc7S2JU',
        ]

        mesages = [
            '1',
            '777',
            '-777',
            '-1',
            'a',
            'Hello',
            'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Quis, voluptatibus quas sequi nesciunt qui obcaecati minus iusto architecto, similique quia, maiores alias itaque! Earum, ut dolor. Quibusdam deserunt aut hic!',
        ]

        for m in mesages:
            for k in keys:
                self.assertEqual(
                    m, decrypt(encrypt(m, k), k),
                    msg=f'key={k} message={m}')

    def test_encrypt_empty_params(self):
        with self.assertRaises(ValueError):
            encrypt('Hello', '')
            encrypt('', 'Hello')
            encrypt('', '')

    def test_decrypt_empty_params(self):
        with self.assertRaises(ValueError):
            decrypt(b'Hello', '')
            decrypt(b'', 'Hello')
            decrypt(b'', '')


__all__ = ['TestEncryption']