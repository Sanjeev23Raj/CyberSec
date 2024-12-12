import re

def password_strength(password):
    """
    Assess the strength of a password based on length, uppercase, lowercase, numbers, and special characters.
    """
    strength_score = 0
    criteria = {
        "length": len(password) >= 8,
        "uppercase": bool(re.search(r"[A-Z]", password)),
        "lowercase": bool(re.search(r"[a-z]", password)),
        "numbers": bool(re.search(r"[0-9]", password)),
        "special": bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)),
    }

    # Calculate the score
    for key, passed in criteria.items():
        if passed:
            strength_score += 1

    # Provide feedback based on the score
    if strength_score == 5:
        strength = "Very Strong"
    elif strength_score == 4:
        strength = "Strong"
    elif strength_score == 3:
        strength = "Moderate"
    elif strength_score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    return strength, criteria


def main():
    print("Password Complexity Checker")
    password = input("Enter a password to check its strength: ")
    strength, criteria = password_strength(password)

    print(f"\nPassword Strength: {strength}")
    print("Criteria Met:")
    print(f"- At least 8 characters: {'✔' if criteria['length'] else '✘'}")
    print(f"- At least one uppercase letter: {'✔' if criteria['uppercase'] else '✘'}")
    print(f"- At least one lowercase letter: {'✔' if criteria['lowercase'] else '✘'}")
    print(f"- At least one number: {'✔' if criteria['numbers'] else '✘'}")
    print(f"- At least one special character: {'✔' if criteria['special'] else '✘'}")


if __name__ == "__main__":
    main()
