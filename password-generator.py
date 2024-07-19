import random
import string

def generate_password(length):
    # Define the character set
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    # Get the desired password length from the user
    while True:
        try:
            length = int(input("Enter the desired length of the password (minimum 6 characters): "))
            if length < 6:
                print("Password length should be at least 6 characters. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    # Generate and display the password
    password = generate_password(length)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()