import cryption


def crypt_service(message):
    message = message.decode()
    print("This is to be crypted:" + message)
    if message.endswith(".create") is True:
        cryption.create_key()
        output = "created key"
    elif message.endswith(".encrypt") is True:
        message = message.removesuffix(".encrypt")
        output = cryption.encrypt(message)
    elif message.endswith(".decrypt") is True:
        message = message.removesuffix(".decrypt")
        output = cryption.decrypt(message)
    else:
        output = "Error"
    return output


if __name__ == "__main__":
    pass
    # selection = "create"
    # message = "Hey, how's it going? Are you doing well?"
    # print(main(message, selection))
    # selection = "encrypt"
    # print(main(message, selection))
    # message = main(message, selection)
    # selection = "decrypt"
    # print(main(message, selection))
