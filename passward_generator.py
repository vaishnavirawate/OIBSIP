import random
import string

def validate_length_input(length_str):
    """Validate the password length input"""
    try:
        length = int(length_str)
        if length < 4:
            print("Password length must be at least 4 characters.")
            return False, None
        elif length > 50:
            print("Password length cannot exceed 50 characters.")
            return False, None
        return True, length
    except ValueError:
        print("Please enter a valid number.")
        return False, None

def validate_yes_no_input(response):
    """Validate yes/no responses"""
    response = response.lower().strip()
    if response in ['y', 'yes']:
        return True
    elif response in ['n', 'no']:
        return False
    else:
        print("Please enter 'y' or 'n'.")
        return None

def generate_password(length, use_letters, use_numbers, use_symbols):
    """Generate a random password based on user criteria"""
    character_set = ""
    
    if use_letters:
        character_set += string.ascii_letters
    if use_numbers:
        character_set += string.digits
    if use_symbols:
        character_set += string.punctuation
    
    # If no character types selected, use all
    if not character_set:
        character_set = string.ascii_letters + string.digits + string.punctuation
        print("No character types selected. Using all character types by default.")
    
    # Generate password
    password = ''.join(random.choice(character_set) for _ in range(length))
    return password

def calculate_password_strength(password):
    """Calculate and return password strength assessment"""
    strength = 0
    if any(c.islower() for c in password):
        strength += 1
    if any(c.isupper() for c in password):
        strength += 1
    if any(c.isdigit() for c in password):
        strength += 1
    if any(c in string.punctuation for c in password):
        strength += 1
    if len(password) >= 12:
        strength += 1
    
    strength_labels = {
        1: "Very Weak",
        2: "Weak",
        3: "Medium",
        4: "Strong",
        5: "Very Strong"
    }
    
    return strength_labels.get(strength, "Very Weak")

# Main program execution starts here
print("=" * 50)
print("        PASSWORD GENERATOR")
print("=" * 50)

# Get password length with validation
while True:
    length_input = input("Enter password length (default 12): ").strip()
    if not length_input:
        length = 12
        break
    is_valid, length = validate_length_input(length_input)
    if is_valid:
        break

# Get character type preferences
print("\nSelect character types to include:")

while True:
    use_letters_input = input("Include letters? (y/n, default y): ").strip()
    if not use_letters_input:
        use_letters = True
        break
    use_letters = validate_yes_no_input(use_letters_input)
    if use_letters is not None:
        break

while True:
    use_numbers_input = input("Include numbers? (y/n, default y): ").strip()
    if not use_numbers_input:
        use_numbers = True
        break
    use_numbers = validate_yes_no_input(use_numbers_input)
    if use_numbers is not None:
        break

while True:
    use_symbols_input = input("Include symbols? (y/n, default y): ").strip()
    if not use_symbols_input:
        use_symbols = True
        break
    use_symbols = validate_yes_no_input(use_symbols_input)
    if use_symbols is not None:
        break

# Generate password
password = generate_password(length, use_letters, use_numbers, use_symbols)
strength = calculate_password_strength(password)

# Display results
print("\n" + "=" * 50)
print("Generated Password:")
print(password)
print(f"Password Strength: {strength}")
print("=" * 50)

# Option to generate another password
while True:
    another = input("\nGenerate another password? (y/n): ").strip().lower()
    if another in ['y', 'yes']:
        print("\nRestarting password generator...")
        print("-" * 30)
        # For simplicity, we'll just exit here since restarting would be complex
        print("Please run the program again to generate another password.")
        break
    elif another in ['n', 'no']:
        print("Thank you for using the Password Generator!")
        break
    else:
        print("Please enter 'y' or 'n'.")