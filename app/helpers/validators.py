import re

EMAIL_REGEX = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w+$")

PASSWORD_REGEX = re.compile(
    r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W_]).{8,}$"
)

def is_valid_email(email: str) -> bool:
    return bool(EMAIL_REGEX.match(email))


def is_strong_password(password: str) -> bool:
    return bool(PASSWORD_REGEX.match(password))
