def text_encryptor(text: str):
    return ''.join([chr(ord(x) + 3) for x in text])


text_to_encrypt = input()
print(text_encryptor(text_to_encrypt))
