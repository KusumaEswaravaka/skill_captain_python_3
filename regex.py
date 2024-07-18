import re

# Initializing regex function
def check_password_strength(password):
    length = 8
    upper_case = re.search(r'[A-Z]', password) is not None
    lower_case = re.search(r'[a-z]', password) is not None
    digits = re.search(r'\d', password) is not None
    special_characters = re.search(r'[!@#$%^&*(),.?":{}<>]', password) is not None
    
    # Score
    score = 0
    score += 1 if len(password) >= length else 0
    score += 1 if upper_case else 0
    score += 1 if lower_case else 0
    score += 1 if digits else 0
    score += 1 if special_characters else 0
    
    return score

# Main
def main():
    password = "HardC0ded@Password123"
    
    score = check_password_strength(password)
    
    # Feedback
    if score == 5:
        print("Password strength: Your password is very strong.")
    elif score == 4:
        print("Password strength: Your password is strong.")
    elif score == 3:
        print("Password strength: Your password is medium strength.")
    elif score == 2:
        print("Password strength: Your password is weak.")
    else:
        print("Password strength: Your password is very weak.")

if __name__ == "__main__":
    main()
# code successfully completed
