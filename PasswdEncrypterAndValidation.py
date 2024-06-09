import hashlib


def encrypt_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def validation_password(password):
    global message
    requiredSym = ['#', '$', '%', '@']
    if len(password) < 8:
        message = 'Hasło musi mieć przynajmniej 8 znaków'
        return False, message
    elif len(password) > 20:
        message = 'Hasło może mieć długość maksymalnie 20 znaków'
        return False, message
    elif not any(char.isdigit() for char in password):
        message = 'Hasło musi zawierać przynajmniej jedną cyfrę'
        return False, message
    elif not any(char.isupper() for char in password):
        message = "hasło musi zawierać przynajmniej jedną duża literę"
        return False, message
    elif not any(char.islower() for char in password):
        message = "hasło musi zawierać przynajmniej jedną małą literę"
        return False, message
    elif not any(char in requiredSym for char in password):
        message = "hasło musi zawierać przynajmniej jeden znak specjalny: #, $, %, @"
        return False, message
    else:
        message = "Hasło jest poprawne"
        return True, message