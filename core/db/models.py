import os

from contextlib import contextmanager
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from dotenv import load_dotenv

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
    available_yahoo = Column(Boolean)
    available_hotmail = Column(Boolean)
    available_gmail = Column(Boolean)
    amazon_check = Column(Boolean)
    twitter_check = Column(Boolean)
    instagram_check = Column(Boolean)
    spotify_check = Column(Boolean)
    pinterest_check = Column(Boolean)
    tumblr_check = Column(Boolean)
    last_fm_check = Column(Boolean)
    social_count = Column(Integer, default=0)


Base.metadata.create_all(engine)
