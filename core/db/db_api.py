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
    """
    Database api class
    """
    def __init__(self):
        self.session = session

    def set_available_amazon(self, email: str):
        """
        Updates or creates a record with a unique field email
        sets the amazon_check field to True
        update social_count field (+=1)
        saves changes to the database

        :param email: unique insert field
        :return:
        """
        with self.session() as s:
            email_obj = s.query(EmailChecker).filter(EmailChecker.email == email).first()
            if not email_obj:
                email_obj = EmailChecker(email=email)
            email_obj.amazon_check = True
            s.add(email_obj)
            s.commit()

    def set_available_twitter(self, email: str):
        """
        Updates or creates a record with a unique field email
        sets the twitter_check field to True
        update social_count field (+=1)
        saves changes to the database

        :param email: unique insert field
        :return:
        """
        with self.session() as s:
            email_obj = s.query(EmailChecker).filter(EmailChecker.email == email).first()
            if not email_obj:
                email_obj = EmailChecker(email=email)
            email_obj.twitter_check = True
            s.add(email_obj)
            s.commit()

    def set_available_yahoo(self, email: str):
        """
        Updates or creates a record with a unique field email
        sets the available_yahoo field to True
        saves changes to the database

        :param email: unique insert field
        :return:
        """
        with self.session() as s:
            email_obj = s.query(EmailChecker).filter(EmailChecker.email == email).first()
            if not email_obj:
                email_obj = EmailChecker(email=email)
            email_obj.available_yahoo = True
            s.add(email_obj)
            s.commit()

    def set_available_hotmail(self, email: str):
        """
        Updates or creates a record with a unique field email
        sets the available_hotmail field to True
        saves changes to the database

        :param email: unique insert field
        :return:
        """
        with self.session() as s:
            email_obj = s.query(EmailChecker).filter(EmailChecker.email == email).first()
            if not email_obj:
                email_obj = EmailChecker(email=email)
            email_obj.available_hotmail = True
            s.add(email_obj)
            s.commit()

    def set_available_gmail(self, email: str):
        """
        Updates or creates a record with a unique field email
        sets the available_gmail field to True
        saves changes to the database

        :param email: unique insert field
        :return:
        """
        with self.session() as s:
            email_obj = s.query(EmailChecker).filter(EmailChecker.email == email).first()
            if not email_obj:
                email_obj = EmailChecker(email=email)
            email_obj.available_gmail = True
            s.add(email_obj)
            s.commit()

    def set_available_instagram(self, email: str):
        """
        Updates or creates a record with a unique field email
        sets the instagram_check field to True
        update social_count field (+=1)
        saves changes to the database

        :param email: unique insert field
        :return:
        """
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
        """
        Updates or creates a record with a unique field email
        sets the spotify_check field to True
        update social_count field (+=1)
        saves changes to the database

        :param email: unique insert field
        :return:
        """
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
        """
        Updates or creates a record with a unique field email
        sets the tumblr_check field to True
        update social_count field (+=1)
        saves changes to the database

        :param email: unique insert field
        :return:
        """
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
        """
        Updates or creates a record with a unique field email
        sets the pinterest_check field to True
        update social_count field (+=1)
        saves changes to the database

        :param email: unique insert field
        :return:
        """
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
        """
        Updates or creates a record with a unique field email
        sets the last_fm_check field to True
        update social_count field (+=1)
        saves changes to the database

        :param email: unique insert field
        :return:
        """
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

    def get_emails(self) -> list:
        """
        Returns models sorted by social_count fields desc

        :return list:
        """

        with self.session() as s:
            return s.query(EmailChecker).order_by(EmailChecker.social_count.desc()).all()


data_api = DataApi()
