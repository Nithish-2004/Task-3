import re

def password_strength_checker(password):
    # Criteria patterns
    length_criteria = re.compile(r'.{8,}')  # At least 8 characters
    uppercase_criteria = re.compile(r'[A-Z]')  # At least one uppercase letter
    lowercase_criteria = re.compile(r'[a-z]')  # At least one lowercase letter
    number_criteria = re.compile(r'\d')  # At least one number
    special_char_criteria = re.compile(r'[\W_]')  # At least one special character

    # Check criteria
    length = bool(length_criteria.search(password))
    uppercase = bool(uppercase_criteria.search(password))
    lowercase = bool(lowercase_criteria.search(password))
    number = bool(number_criteria.search(password))
    special_char = bool(special_char_criteria.search(password))

    # Count the number of fulfilled criteria
    criteria_fulfilled = sum([length, uppercase, lowercase, number, special_char])

    # Determine the strength of the password
    if criteria_fulfilled == 5:
        strength = "Very Strong"
    elif criteria_fulfilled == 4:
        strength = "Strong"
    elif criteria_fulfilled == 3:
        strength = "Medium"
    else:
        strength = "Weak"

    # Provide feedback
    feedback = []
    if not length:
        feedback.append("Password should be at least 8 characters long.\n")
    if not uppercase:
        feedback.append("Password should contain at least one uppercase letter.\n")
    if not lowercase:
        feedback.append("Password should contain at least one lowercase letter.\n")
    if not number:
        feedback.append("Password should contain at least one number.\n")
    if not special_char:
        feedback.append("Password should contain at least one special character.\n")

    return strength, feedback


# Example usage
if __name__ == "__main__":
    password = input("Enter a password to check its strength: ")
    strength, feedback = password_strength_checker(password)
    print(f"Password strength: {strength}")
    if feedback:
        print("Feedback:")
        for item in feedback:
            print(f"- {item}")
