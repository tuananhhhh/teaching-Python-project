import random
import string

def generate_password(length):
    # Define the character sets for the password
    letters = string.ascii_letters
    digits = string.digits
    punctuation = string.punctuation

    # Ensure at least one character from each category is in the password
    password = random.choice(letters) + random.choice(digits) + random.choice(punctuation) + ''.join(random.choice(string.printable) for _ in range(length - 3))
    

    # Shuffle the characters to make the password random
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password

if __name__ == "__main__":
    # Set the desired length for your password
    password_length = int(input('What is the length of the password: \n'))  # You can type your preferred length

    # Generate and print a random password
    password = generate_password(password_length)
    print("Generated Password:", password)
