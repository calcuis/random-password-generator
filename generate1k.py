import random
import string

def generate_password(length=10):
    if length < 4:  # Ensure the password length is at least 4 to include all character types
        raise ValueError("Password length must be at least 4 characters.")
    
    # Define character pools
    upper_case = string.ascii_uppercase
    lower_case = string.ascii_lowercase
    digits = string.digits
    special_chars = string.punctuation
    
    # Ensure the password contains at least one of each character type
    password = [
        random.choice(upper_case),
        random.choice(lower_case),
        random.choice(digits),
        random.choice(special_chars)
    ]
    
    # Fill the remaining characters randomly from all pools
    all_chars = upper_case + lower_case + digits + special_chars
    password += random.choices(all_chars, k=length-4)
    
    # Shuffle the password list to ensure randomness
    random.shuffle(password)
    
    # Convert the list to a string and return it
    return ''.join(password)

def generate_multiple_passwords(count=1000, length=10):
    passwords = [generate_password(length) for _ in range(count)]
    return passwords

# Generate 1000 random passwords of length 10
passwords = generate_multiple_passwords()
for i, pwd in enumerate(passwords):
    print(f"Password {i+1}: {pwd}")
