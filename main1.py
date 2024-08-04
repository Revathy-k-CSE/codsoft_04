import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("PASSWORD GENERATOR")

    while True:
        try:
            length = int(input("Enter the desired length of your password: "))

            if length <= 7:
                print("Length must be greater than seven. Please try again.")
                continue

            password = generate_password(length)
            print("The generated password is:", password)
            break

        except ValueError:
            print("Invalid input")

if __name__ == "__main__":
    main()
