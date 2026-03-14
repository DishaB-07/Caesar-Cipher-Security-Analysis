def encrypt(text, shift):
    result = ""
    for char in text.upper():
        if char.isalpha():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            result += char
    return result


def decrypt(text, shift):
    result = ""
    for char in text.upper():
        if char.isalpha():
            result += chr((ord(char) - 65 - shift) % 26 + 65)
        else:
            result += char
    return result


def brute_force_attack(cipher_text):
    print("\n--- Brute Force Attack Results ---\n")
    for key in range(1, 26):
        decrypted_text = decrypt(cipher_text, key)
        print(f"Key {key:2} : {decrypted_text}")


def frequency_analysis(cipher_text):
    freq = {}
    for char in cipher_text.upper():
        if char.isalpha():
            freq[char] = freq.get(char, 0) + 1

    most_frequent = max(freq, key=freq.get)
    guessed_key = (ord(most_frequent) - ord('E')) % 26
    decrypted_text = decrypt(cipher_text, guessed_key)

    print("\nLetter Frequency:", freq)
    print("Most Frequent Letter:", most_frequent)
    print("Guessed Key:", guessed_key)
    print("Decrypted Text (Guessed):", decrypted_text)
    print("\nNote: Frequency analysis works best for long encrypted text.")


def main():
    print("\nCAESAR CIPHER SECURITY ANALYSIS")
    print("1. Encrypt & Decrypt")
    print("2. Brute Force Attack")
    print("3. Frequency Analysis Attack")

    choice = input("\nEnter your choice (1/2/3): ")

    if choice == '1':
        message = input("Enter message: ")
        shift = int(input("Enter shift value: "))
        encrypted = encrypt(message, shift)
        decrypted = decrypt(encrypted, shift)
        print("\nEncrypted Text:", encrypted)
        print("Decrypted Text:", decrypted)

    elif choice == '2':
        cipher_text = input("Enter encrypted message: ")
        brute_force_attack(cipher_text)

    elif choice == '3':
        cipher_text = input("Enter encrypted message: ")
        frequency_analysis(cipher_text)

    else:
        print("Invalid choice!")


main()