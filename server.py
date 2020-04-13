import socket
import sys
import os
sys.path.append(os.getcwd())

from crypto.diffie_hellman import DiffieHellman
from crypto.xor_cipher import encrypt, decrypt
import config


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('127.0.0.1', 31337)
sock.bind(server_address)
sock.listen()

while True:
    try:
        connection, client_address = sock.accept()

        # sending the server public key to the client
        dh = DiffieHellman(config.GENERATOR, config.PRIME_DIVIDER)
        connection.sendall(str(dh.public_key).encode('utf8'))

        # recive the client public key
        client_public_key = int(connection.recv(4096).decode('utf8'))
        print(f'the client {client_address} sended public_key: {client_public_key}')

        # make the secret key
        secret_key = str(dh.make_secret(client_public_key))

        # send the cipher text to the client
        connection.sendall(encrypt('ping', secret_key))

        # recv the cipher text from the client
        cipher_text = connection.recv(4096)

        # decrypt the cipher text
        plain_text = decrypt(cipher_text, secret_key)
        print(f'the client {client_address} sended {plain_text}')
    finally:
        connection.close()