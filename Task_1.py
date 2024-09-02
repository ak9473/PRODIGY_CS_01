 
def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    
    if mode == 'decrypt':
        shift = -shift

    for char in text:

        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
           
            result += char

    return result

def main():
    print("Caesar Cipher Program")
    mode = input("Enter 'e' for encryption or 'd' for decryption: ").lower()
    if mode not in ['e', 'd']:
        print("Invalid mode. Please enter 'e' for encryption or 'd' for decryption.")
        return

    message = input("Enter your message: ")
    try:
        shift = int(input("Enter the shift value (positive integer): "))
        if shift < 0:
            print("Shift value must be a positive integer.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid integer for the shift value.")
        return

    if mode == 'e':
        encrypted_message = caesar_cipher(message, shift, 'encrypt')
        print(f"Encrypted Message: {encrypted_message}")
    else:
        decrypted_message = caesar_cipher(message, shift, 'decrypt')
        print(f"Decrypted Message: {decrypted_message}")

if __name__ == "__main__":
    main()
