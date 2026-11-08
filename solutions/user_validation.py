def validate_user(name, email, age):
    if not name or not email or age < 18:
        return False

    return True


def validate_registration(name, email, age):
    return validate_user(name, email, age)