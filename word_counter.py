try:
    file_name = input("Enter the file name: ")

    with open(file_name, "r") as file:
        content = file.read()

    words = content.split()
    word_count = len(words)

    print(f"Total number of words: {word_count}")

except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print(f"An error occurred: {e}")