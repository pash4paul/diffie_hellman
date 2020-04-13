import socket
import sys
import os
sys.path.append(os.getcwd())

from crypto.diffie_hellman import DiffieHellman
from crypto.xor_cipher import encrypt, decrypt
import config


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('127.0.0.1', 31337)
sock.connect(server_address)

try:
    # sending the client public key to the server
    dh = DiffieHellman(config.GENERATOR, config.PRIME_DIVIDER)
    sock.sendall(str(dh.public_key).encode('utf8'))

    # recive the server public key
    server_public_key = int(sock.recv(4096).decode('utf8'))
    print(f'the server {server_address} sended public_key: {server_public_key}')

    # make the secret key
    secret_key = str(dh.make_secret(server_public_key))

    # send the cipher text to the server
    sock.sendall(encrypt('pong', secret_key))

    # recv the cipher text from the server
    cipher_text = sock.recv(4096)

    # decrypt the cipher text
    plain_text = decrypt(cipher_text, secret_key)
    print(f'the server {server_address} sended {plain_text}')
finally:
    sock.close()