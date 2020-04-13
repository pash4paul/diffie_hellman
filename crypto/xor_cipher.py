from itertools import cycle
import functools


def check_params(func):
    @functools.wraps(func)
    def wrapper(text, key):
        if not text:
            raise ValueError('text must not be empty')
        elif not key:
            raise ValueError('key must not be empty')
        return func(text, key)
    return wrapper


@check_params
def encrypt(plain_text: str, key: str) -> bytes:
    plain_text_b = plain_text.encode('utf8')
    key_b = cycle(key.encode('utf8'))
    res = bytes([a ^ b for a, b in zip(plain_text_b, key_b)])
    return res


@check_params
def decrypt(cipher_text_b: bytes, key: str) -> str:
    key_b = cycle(key.encode('utf8'))
    plain_text_b = bytes([a ^ b for a, b in zip(cipher_text_b, key_b)])
    return plain_text_b.decode('utf8')