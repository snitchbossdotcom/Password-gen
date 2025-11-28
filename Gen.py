import secrets
import string
import sys

def generate_password(length, include_uppercase, include_lowercase, include_digits, include_symbols):
    character_sets = ''
    if include_uppercase:
        character_sets += string.ascii_uppercase
    if include_lowercase:
        character_sets += string.ascii_lowercase
    if include_digits:
        character_sets += string.digits
    if include_symbols:
        character_sets += string.punctuation

    if not character_sets:
        print("Error: Please select at least one character set.", file=sys.stderr)
        return None

    password = ''.join(secrets.choice(character_sets) for _ in range(length))
    return password

def main():
    try:
        length_str = input("Enter the desired password length (minimum 8): ")
        length = int(length_str)
        if length < 8:
            print("Password length must be at least 8. Using default length of 12.", file=sys.stderr)
            length = 12
    except ValueError:
        print("Invalid input. Please enter a number. Using default length of 12.", file=sys.stderr)
        length = 12

    include_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    include_lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
    include_digits = input("Include digits? (yes/no): ").lower() == 'yes'
    include_symbols = input("Include symbols? (yes/no): ").lower() == 'yes'

    generated_password = generate_password(length, include_uppercase, include_lowercase, include_digits, include_symbols)

    if generated_password:
        print("\nYour password is:")
        print(generated_password)

if __name__ == "__main__":
    main()
      
