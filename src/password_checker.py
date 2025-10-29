import re

def check_password_strength(password: str) -> str:
    """
    Evaluates the strength of a password based on:
    - Length
    - Uppercase/lowercase letters
    - Numbers
    - Special characters
    """

    # Minimum length requirement
    if len(password) < 8:
        return "Weak: Password should be at least 8 characters long."

    # Check patterns
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'[0-9]', password))
    has_special = bool(re.search(r'[^A-Za-z0-9]', password))

    # Evaluate strength
    strength_score = sum([has_upper, has_lower, has_digit, has_special])

    if strength_score == 4:
        return "Strong: Great job! Your password is strong."
    elif strength_score == 3:
        return "Medium: Add more variety (e.g., special characters or numbers)."
    else:
        return "Weak: Try mixing uppercase, lowercase, numbers, and symbols."

if __name__ == "__main__":
    print("🔐 Password Strength Checker 🔐\n")
    while True:
        pwd = input("Enter a password to test (or type 'exit' to quit): ")
        if pwd.lower() == "exit":
            break
        result = check_password_strength(pwd)
        print(result)
        print("-" * 50)
