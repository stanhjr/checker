from core.db.models import session, EmailChecker
from functools import wraps


def with_session(function):
    @wraps(function)
    def context_session(*args, **kwargs):
        with session() as s:
            kwargs['s'] = s
            return function(*args, **kwargs)

    return context_session


class DataApi:
    def __init__(self):
        self.session = session

    def set_available_amazon(self, email: str):
        with self.session() as s:
            email_obj = s.query(EmailChecker).filter(EmailChecker.email == email).first()
            if not email_obj:
                email_obj = EmailChecker(email=email)
            email_obj.amazon_check = True
            s.add(email_obj)
            s.commit()

    def set_available_twitter(self, email: str):
        with self.session() as s:
            email_obj = s.query(EmailChecker).filter(EmailChecker.email == email).first()
            if not email_obj:
                email_obj = EmailChecker(email=email)
            email_obj.twitter_check = True
            s.add(email_obj)
            s.commit()

    def set_available_yahoo(self, email: str):
        with self.session() as s:
            email_obj = s.query(EmailChecker).filter(EmailChecker.email == email).first()
            if not email_obj:
                email_obj = EmailChecker(email=email)
            email_obj.available_yahoo = True
            s.add(email_obj)
            s.commit()

    def set_available_hotmail(self, email: str):
        with self.session() as s:
            email_obj = s.query(EmailChecker).filter(EmailChecker.email == email).first()
            if not email_obj:
                email_obj = EmailChecker(email=email)
            email_obj.available_hotmail = True
            s.add(email_obj)
            s.commit()

    def set_available_gmail(self, email: str):
        with self.session() as s:
            email_obj = s.query(EmailChecker).filter(EmailChecker.email == email).first()
            if not email_obj:
                email_obj = EmailChecker(email=email)
            email_obj.available_gmail = True
            s.add(email_obj)
            s.commit()

    def set_available_instagram(self, email: str):
        with self.session() as s:
            email_obj = s.query(EmailChecker).filter(EmailChecker.email == email).first()
            if not email_obj:
                email_obj = EmailChecker(email=email)
                email_obj.social_count = 0
            if not  email_obj.instagram_check:
                email_obj.social_count = email_obj.social_count + 1
            email_obj.instagram_check = True

            s.add(email_obj)
            s.commit()

    def set_available_spotify(self, email: str):
        with self.session() as s:
            email_obj = s.query(EmailChecker).filter(EmailChecker.email == email).first()
            if not email_obj:
                email_obj = EmailChecker(email=email)
                email_obj.social_count = 0
            if not email_obj.spotify_check:
                email_obj.social_count = email_obj.social_count + 1
            email_obj.spotify_check = True
            s.add(email_obj)
            s.commit()

    def set_available_tumblr(self, email: str):
        with self.session() as s:
            email_obj = s.query(EmailChecker).filter(EmailChecker.email == email).first()
            if not email_obj:
                email_obj = EmailChecker(email=email)
                email_obj.social_count = 0
            if not email_obj.tumblr_check:
                email_obj.social_count = email_obj.social_count + 1
            email_obj.tumblr_check = True
            s.add(email_obj)
            s.commit()

    def set_available_pinterest(self, email: str):
        with self.session() as s:
            email_obj = s.query(EmailChecker).filter(EmailChecker.email == email).first()
            if not email_obj:
                email_obj = EmailChecker(email=email)
                email_obj.social_count = 0
            if not email_obj.pinterest_check:
                email_obj.social_count = email_obj.social_count + 1
            email_obj.pinterest_check = True
            s.add(email_obj)
            s.commit()

    def set_available_last_fm(self, email: str):
        with self.session() as s:
            email_obj = s.query(EmailChecker).filter(EmailChecker.email == email).first()
            if not email_obj:
                email_obj = EmailChecker(email=email)
                email_obj.social_count = 0
            if not email_obj.last_fm_check:
                email_obj.social_count = email_obj.social_count + 1
            email_obj.last_fm_check = True
            s.add(email_obj)
            s.commit()

    def get_emails(self):
        with self.session() as s:
            return s.query(EmailChecker).order_by(EmailChecker.social_count.desc()).all()


data_api = DataApi()
