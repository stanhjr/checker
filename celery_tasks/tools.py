
def converting_email(email: str, type_email: str = '@yahoo.com'):
    """
    Checked and converted the email to a valid form

    :param email: email to check
    :param type_email: email type
    :return:
    """

    if not email.find(type_email) > 0:
        return False
    email = email.strip()
    list_ = email.split('@')
    if len(list_) < 2:
        return False
    if list_[1].find(type_email[1:]) < 0:
        return False
    email_valid = f"{list_[0]}@{list_[1]}"
    slice_email = len(list_[0]) + len(type_email)
    return email_valid[:slice_email]


def check_email_valid(email: str) -> bool:
    email = email.strip()
    if email.find('@gmail.com') > 0:
        return True
    if email.find('@yahoo.com') > 0:
        return True
    if email.find('@hotmail.com') > 0:
        return True
    if email.find('aol.com') > 0:
        return True
    if email.find('outlook.com') > 0:
        return True
    return False
