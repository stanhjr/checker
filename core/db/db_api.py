from core.db.db_tools import calculate_register_social_media, string_date_to_datetime, timestamp_to_datetime
from core.db.models import Session, EmailChecker

from core.schemas import EmailCheckerScraper


class DataApi:
    """
    Database api class
    """
    def __init__(self):
        self.session = Session

    def set_checker_result(self, scraper: EmailCheckerScraper):
        """
        Updates or creates a record with a unique field email
        update social_count field (+=1)
        saves changes to the database

        :param scraper: unique insert field
        :param response_dict:
        :return:
        """
        with self.session() as s:
            email_obj = s.query(EmailChecker).filter(EmailChecker.email == scraper.email).first()
            if not email_obj:
                email_obj = EmailChecker(email=scraper.email)
            email_obj.adobe = scraper.account_details.adobe.registered
            email_obj.apple = scraper.account_details.apple.registered
            email_obj.airbnb = scraper.account_details.airbnb.registered
            email_obj.amazon = scraper.account_details.amazon.registered
            email_obj.atlassian = scraper.account_details.atlassian.registered
            email_obj.archiveorg = scraper.account_details.archiveorg.registered
            email_obj.booking = scraper.account_details.booking.registered
            email_obj.bukalapak = scraper.account_details.bukalapak.registered
            email_obj.flickr = scraper.account_details.flickr.registered
            email_obj.foursquare = scraper.account_details.foursquare.registered
            email_obj.facebook = scraper.account_details.facebook.registered
            email_obj.discord = scraper.account_details.discord.registered
            email_obj.disneyplus = scraper.account_details.disneyplus.registered
            email_obj.ebay = scraper.account_details.ebay.registered
            email_obj.envato = scraper.account_details.envato.registered
            email_obj.evernote = scraper.account_details.evernote.registered
            email_obj.github = scraper.account_details.github.registered
            email_obj.google = scraper.account_details.google.registered
            email_obj.gravatar = scraper.account_details.gravatar.registered
            email_obj.imgur = scraper.account_details.imgur.registered
            email_obj.instagram = scraper.account_details.instagram.registered
            email_obj.jdid = scraper.account_details.jdid.registered
            email_obj.kakao = scraper.account_details.kakao.registered
            email_obj.lastfm = scraper.account_details.lastfm.registered
            email_obj.lazada = scraper.account_details.lazada.registered
            email_obj.linkedin = scraper.account_details.linkedin.registered
            email_obj.mailru = scraper.account_details.mailru.registered
            email_obj.myspace = scraper.account_details.myspace.registered
            email_obj.microsoft = scraper.account_details.microsoft.registered
            email_obj.netflix = scraper.account_details.netflix.registered
            email_obj.ok = scraper.account_details.ok.registered
            email_obj.patreon = scraper.account_details.patreon.registered
            email_obj.pinterest = scraper.account_details.pinterest.registered
            email_obj.quora = scraper.account_details.quora.registered
            email_obj.qzone = scraper.account_details.qzone.registered
            email_obj.rambler = scraper.account_details.rambler.registered
            email_obj.samsung = scraper.account_details.samsung.registered
            email_obj.skype = scraper.account_details.skype.registered
            email_obj.spotify = scraper.account_details.spotify.registered
            email_obj.tumblr = scraper.account_details.tumblr.registered
            email_obj.twitter = scraper.account_details.twitter.registered
            email_obj.tokopedia = scraper.account_details.tokopedia.registered
            email_obj.vimeo = scraper.account_details.vimeo.registered
            email_obj.weibo = scraper.account_details.weibo.registered
            email_obj.wordpress = scraper.account_details.wordpress.registered
            email_obj.yahoo = scraper.account_details.yahoo.registered
            email_obj.zoho = scraper.account_details.zoho.registered
            email_obj.score = scraper.score
            email_obj.email = scraper.email
            email_obj.first_breach = string_date_to_datetime(scraper.breach_details.first_breach)
            email_obj.first_seen = timestamp_to_datetime(scraper.history.first_seen)
            email_obj.social_count = calculate_register_social_media(scraper.account_details.dict())
            s.add(email_obj)
            s.commit()
            return True

    def get_emails(self) -> list:
        """
        Returns models sorted by social_count fields desc

        :return list:
        """

        with self.session() as s:
            return s.query(EmailChecker).order_by(EmailChecker.social_count.desc()).all()

    def get_results(self) -> list:
        """
        Gets emails parse results from database
        :return list:
        """
        with self.session() as s:
            qs = s.query(EmailChecker).order_by(EmailChecker.social_count.desc()).all()
            return [model.get_model_dict() for model in qs]


data_api = DataApi()
