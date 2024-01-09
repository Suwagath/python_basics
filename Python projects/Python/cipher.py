# Original encrypted text and custom key
text = 'mrttaqrhknsw ih puggrur'
custom_key = 'python'

# Function to perform Vigenere encryption or decryption
def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():

        # Append any non-letter character to the message
        if not char.isalpha():
            final_message += char
        else:        
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset * direction) % len(alphabet)
            final_message += alphabet[new_index]
    
    return final_message

# Function to encrypt a message using Vigenere cipher
def encrypt(message, key):
    return vigenere(message, key)
    
# Function to decrypt a message using Vigenere cipher
def decrypt(message, key):
    return vigenere(message, key, -1)

# Display original, encrypted, and decrypted text
print(f'\nOriginal text: {text}')
print(f'Key: {custom_key}')

# Encrypt the original text using the custom key
encryption = encrypt(text, custom_key)
print(f'\nEncrypted text: {encryption}')

# Decrypt the encrypted text using the custom key
decryption = decrypt(encryption, custom_key)
print(f'Decrypted text: {decryption}\n')
