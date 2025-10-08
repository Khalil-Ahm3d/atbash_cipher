def atbash_cipher(text):
    """Encrypt or decrypt text using the Atbash cipher."""
    result = ""

    for char in text:
        if char.isalpha():
            # Handle uppercase letters (A–Z)
            if char.isupper():
                result += chr(155 - ord(char))  # 65 + 90 = 155
            # Handle lowercase letters (a–z)
            else:
                result += chr(219 - ord(char))  # 97 + 122 = 219
        else:
            # Preserve non-alphabetic characters
            result += char

    return result


if __name__ == "__main__":
    print("=== Atbash Cipher Program ===")
    plaintext = input("Enter text to encrypt: ")

    encrypted_text = atbash_cipher(plaintext)
    print("\nEncrypted text:", encrypted_text)

    decrypted_text = atbash_cipher(encrypted_text)
    print("Decrypted text:", decrypted_text)
