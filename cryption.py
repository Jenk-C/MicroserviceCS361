import sys
from cryptography.fernet import Fernet


def create_key():
    key = Fernet.generate_key()
    file = open('key.txt', 'w')
    file.write(key.decode())


def encrypt(message):
    file = open('key.txt', 'r')
    key = file.read()
    f = Fernet(key.encode('ascii'))
    output = f.encrypt(message.encode('ascii'))
    return output


def decrypt(message):
    file = open('key.txt', 'r')
    key = file.read()
    f = Fernet(key.encode('ascii'))
    byteoutput = f.decrypt(message.encode('ascii'))
    output = byteoutput
    return output
