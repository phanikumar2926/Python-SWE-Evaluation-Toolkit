def validate_user(name, email, age):
    if name is None:
        return False
    if name == "":
        return False
    if email is None:
        return False
    if email == "":
        return False
    if age < 18:
        return False
    return True


def validate_registration(name, email, age):
    if name is None:
        return False
    if name == "":
        return False
    if email is None:
        return False
    if email == "":
        return False
    if age < 18:
        return False
    return True