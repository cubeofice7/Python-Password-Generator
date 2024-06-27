import random
import string

def generate_password(length, use_lower=True, use_upper=True, use_digits=True, use_special=True):
    # Define character sets
    lower_chars = string.ascii_lowercase  # abcdefghijklmnopqrstuvwxyz
    upper_chars = string.ascii_uppercase  # ABCDEFGHIJKLMNOPQRSTUVWXYZ
    digit_chars = string.digits  # 0123456789
    special_chars = string.punctuation  # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

    # Initialize character set for password generation
    chars = []
    if use_lower:
        chars.extend(list(lower_chars))
    if use_upper:
        chars.extend(list(upper_chars))
    if use_digits:
        chars.extend(list(digit_chars))
    if use_special:
        chars.extend(list(special_chars))

    # Check if at least one character set is chosen
    if not (use_lower or use_upper or use_digits or use_special):
        raise ValueError("At least one character set must be chosen.")

    # Generate the password
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    try:
        length = int(input("Enter the length of the password: "))
        use_lower = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
        use_upper = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
        use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
        use_special = input("Include special characters? (yes/no): ").lower() == 'yes'

        password = generate_password(length, use_lower, use_upper, use_digits, use_special)
        print(f"Generated Password: {password}")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()