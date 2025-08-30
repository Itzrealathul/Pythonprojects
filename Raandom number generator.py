import random
import string
def generate_password(length=12):
    if length < 6:
        return "Password length should be at least 6 characters."
    lower = random.choice(string.ascii_lowercase)
    upper = random.choice(string.ascii_uppercase)
    digit = random.choice(string.digits)
    all_chars = string.ascii_letters + string.digits
    remaining = [random.choice(all_chars) for _ in range(length - 3)]
    password_list = list(lower + upper + digit + ''.join(remaining))
    random.shuffle(password_list)
    password = ''.join(password_list)
    return password
print("Generated Password:", generate_password(12))