import math
import re
import getpass
from pathlib import Path


def load_common_passwords():
    file_path = Path(__file__).with_name("common_passwords.txt")

    if not file_path.exists():
        return {"password", "123456", "qwerty", "admin"}

    return {
        line.strip().lower()
        for line in file_path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    }


def estimate_entropy(password):
    """Estimate entropy using character variety and length."""

    pool_size = 0

    if any(c.islower() for c in password):
        pool_size += 26
    if any(c.isupper() for c in password):
        pool_size += 26
    if any(c.isdigit() for c in password):
        pool_size += 10
    if any(not c.isalnum() for c in password):
        pool_size += 33

    if pool_size == 0:
        return 0.0

    return len(password) * math.log2(pool_size)


def check_password(password):
    common_passwords = load_common_passwords()
    score = 0
    feedback = []

    # Check length
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
        feedback.append("Use at least 12 characters.")
    else:
        feedback.append("Your password is too short.")

    # Check character variety
    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Consider adding uppercase letters.")

    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("Consider adding lowercase letters.")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Consider adding numbers.")

    if any(not c.isalnum() for c in password):
        score += 1
    else:
        feedback.append("Consider adding special characters.")

    # Check common passwords
    if password.lower() in common_passwords:
        return {
            "strength": "Very Weak",
            "score": 0,
            "entropy": 0.0,
            "feedback": [
                "This is a commonly used password. Choose a different one."
            ],
        }

    # Check repeated characters
    if len(password) >= 3 and len(set(password)) == 1:
        score = 0
        feedback.append("Avoid repeating the same character.")

    # Check simple sequences
    if re.search(
        r"0123|1234|2345|3456|4567|5678|6789|abcd|qwerty",
        password.lower(),
    ):
        score = max(0, score - 2)
        feedback.append("Avoid predictable sequences.")

    # Estimate entropy
    entropy = estimate_entropy(password)

    # Assign strength
    if len(password) < 8 or score <= 2:
        strength = "Weak"
    elif len(password) >= 12 and score >= 5:
        strength = "Strong"
    else:
        strength = "Moderate"

    if not feedback:
        feedback.append("Good start. Avoid reused passwords and personal details.")

    return {
        "strength": strength,
        "score": score,
        "entropy": round(entropy, 2),
        "feedback": feedback,
    }


def main():
    print("=== Password Strength Checker ===")
    print("Your password is checked locally and is not saved.")

    password = getpass.getpass("Enter a test password: ")

    result = check_password(password)

    print("\n--- Results ---")
    print("Strength:", result["strength"])
    print("Score:", result["score"], "/ 6")
    print("Estimated entropy:", result["entropy"], "bits")

    print("\nSuggestions:")
    for suggestion in result["feedback"]:
        print("-", suggestion)

    # Do not print or save the entered password.


if __name__ == "__main__":
    main()