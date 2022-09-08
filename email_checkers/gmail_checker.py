import requests


def gmail_checker(email) -> bool:
    req = requests.Session()
    request = req.get('https://mail.google.com/mail/gxlu?email=' + email)

    if len(request.cookies) > 0:
        return True

print(gmail_checker("stanhjrpow22222er@gmail.com"))


