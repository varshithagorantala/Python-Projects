def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            if char.islower():
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            result += char

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


choice = input("Enter E for Encrypt or D for Decrypt: ").upper()

input_file = input("Enter file name: ")
shift = 3

try:
    with open(input_file, "r") as file:
        content = file.read()

    if choice == "E":
        result = encrypt(content, shift)
        output_file = "encrypted.txt"

    elif choice == "D":
        result = decrypt(content, shift)
        output_file = "decrypted.txt"

    else:
        print("Invalid choice.")
        exit()

    with open(output_file, "w") as file:
        file.write(result)

    print(f"Operation successful!")
    print(f"Output saved in {output_file}")

except FileNotFoundError:
    print("File not found.")