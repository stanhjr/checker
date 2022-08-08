import os

from contextlib import contextmanager
from sqlalchemy import Column, Integer, String, Boolean, Float, DateTime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from dotenv import load_dotenv

from core.db.db_tools import get_datetime_or_none

dotenv_path = ('.env')
load_dotenv(dotenv_path)

Base = declarative_base()
db_settings = "postgresql://postgres:example@localhost:5432/check_email"
engine = create_engine(db_settings, pool_size=50, max_overflow=0, echo=False, echo_pool=True, pool_pre_ping=True)


@contextmanager
def session():
    connection = engine.connect()
    db_session = scoped_session(sessionmaker(autocommit=False, autoflush=True, bind=engine))
    try:
        yield db_session
    except Exception as e:
        print(e)
    finally:
        db_session.remove()
        connection.close()


class EmailChecker(Base):
    __tablename__ = 'emails_checker'
    id = Column(Integer, nullable=False, unique=True, primary_key=True)
    email = Column(String(100), nullable=False, unique=True)
    adobe = Column(Boolean)
    airbnb = Column(Boolean)
    amazon = Column(Boolean)
    apple = Column(Boolean)
    archiveorg = Column(Boolean)
    atlassian = Column(Boolean)
    booking = Column(Boolean)
    bukalapak = Column(Boolean)
    discord = Column(Boolean)
    disneyplus = Column(Boolean)
    ebay = Column(Boolean)
    envato = Column(Boolean)
    evernote = Column(Boolean)
    facebook = Column(Boolean)
    flickr = Column(Boolean)
    flipkart = Column(Boolean)
    foursquare = Column(Boolean)
    github = Column(Boolean)
    google = Column(Boolean)
    gravatar = Column(Boolean)
    imgur = Column(Boolean)
    instagram = Column(Boolean)
    jdid = Column(Boolean)
    kakao = Column(Boolean)
    lastfm = Column(Boolean)
    lazada = Column(Boolean)
    linkedin = Column(Boolean)
    mailru = Column(Boolean)
    microsoft = Column(Boolean)
    myspace = Column(Boolean)
    netflix = Column(Boolean)
    ok = Column(Boolean)
    patreon = Column(Boolean)
    pinterest = Column(Boolean)
    quora = Column(Boolean)
    qzone = Column(Boolean)
    rambler = Column(Boolean)
    samsung = Column(Boolean)
    skype = Column(Boolean)
    spotify = Column(Boolean)
    tokopedia = Column(Boolean)
    tumblr = Column(Boolean)
    twitter = Column(Boolean)
    vimeo = Column(Boolean)
    weibo = Column(Boolean)
    wordpress = Column(Boolean)
    yahoo = Column(Boolean)
    zoho = Column(Boolean)
    score = Column(Float)
    first_breach = Column(DateTime)
    first_seen = Column(DateTime)
    social_count = Column(Integer, default=0)

    def get_social_list(self):
        social_list = []
        columns = self.__table__.columns.keys()
        for key in columns:
            if getattr(self, key) is True:
                social_list.append(key)
        return social_list

    def get_model_dict(self):
        return {"email": self.email,
                "first_breach": get_datetime_or_none(self.first_breach),
                "first_seen ": get_datetime_or_none(self.first_seen),
                "score": self.score,
                "social_count": self.social_count,
                "social_register": self.get_social_list()}


Base.metadata.create_all(engine)
