import random
import string


def generate_password(length, include_ascii):
    characters = string.ascii_letters + string.digits
    # print(characters)
    if include_ascii:
        characters += string.punctuation
    # print(characters)

    password = ''.join(random.choice(characters) for i in range(length))
    return password


def main():
    jafar = int(input("Enter the desired length of the password: "))
    mamad = input("Do you want to include ASCII characters? (yes/no): ").lower() == 'yes'

    if jafar < 1:
        print("Password length should be at least 1")
        return

    password = generate_password(jafar, mamad)
    print("Generated password:", password)


if __name__ == "__main__":
    main()
