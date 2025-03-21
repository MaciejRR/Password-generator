import secrets
import string
import random

def generate_password(length, use_uppercase, use_digits, use_symbols):
    """
    Generuje silne hasło o podanej długości z wybranymi opcjami.

    Parametry:
      length (int): Całkowita długość hasła (minimum 8).
      use_uppercase (bool/int): Jeśli True lub 1, włącza duże litery.
      use_digits (bool/int): Jeśli True lub 1, włącza cyfry.
      use_symbols (bool/int): Jeśli True lub 1, włącza znaki specjalne.

    Zwraca:
      str: Wygenerowane hasło.

    Wyjątki:
      ValueError: Jeśli podana długość jest mniejsza niż 8 lub
                  długość nie pozwala na włączenie gwarantowanych znaków.
    """
    if length < 8:
        raise ValueError("Password must be at least 8 characters long")

    #Małe litery zawsze włączone
    charset = string.ascii_lowercase

    #Dodawanie pozostałych zestawów znaków, jeśli zostały wybrane
    if use_uppercase:
        charset += string.ascii_uppercase
    if use_digits:
        charset += string.digits
    if use_symbols:
        charset += string.punctuation

    #Gwarantujemy, że hasło zawiera przynajmniej jeden znak z każdej wybranej kategorii
    password = [secrets.choice(string.ascii_lowercase)]
    if use_uppercase:
        password.append(secrets.choice(string.ascii_uppercase))
    if use_digits:
        password.append(secrets.choice(string.digits))
    if use_symbols:
        password.append(secrets.choice(string.punctuation))

    #Jeśli podana długość jest mniejsza niż liczba gwarantowanych znaków, rzucamy wyjątek
    if length < len(password):
        raise ValueError("The length entered is too short for the options selected")

    #Uzupełnienie hasła pozostałymi znakami
    while len(password) < length:
        password.append(secrets.choice(charset))

    #Mieszanie znaków, aby było bardziej naturalnie
    random.SystemRandom().shuffle(password)
    return ''.join(password)
