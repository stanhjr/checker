import requests


def gmail_checker(email) -> bool:
    """
    Checks gmail availability

    :param email: email to check
    :return: bool
    """
    req = requests.Session()
    request = req.get('https://mail.google.com/mail/gxlu?email=' + email)

    if len(request.cookies) == 0:
        return True




