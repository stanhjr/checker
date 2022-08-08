from datetime import datetime

from dateutil import parser


def string_date_to_datetime(string_date: str) -> datetime:
    """
    Convert and returns string date to datetime if not string date returns none

    :param: str: string_date
    :return: datetime object
    """
    if isinstance(string_date, str):
        return parser.parse(string_date)


def timestamp_to_datetime(timestamp: int) -> datetime:
    """
    Convert and returns timestamp to datetime if not string date returns none

    :param: int: timestamp
    :return: datetime object
    """
    if isinstance(timestamp, int):
        return datetime.utcfromtimestamp(timestamp)


def calculate_register_social_media(social_dict: dict) -> int:
    """
    Calculates register social media and returns count of register
    :param social_dict: Dictionary social media
    :return: int: count of register
    """
    result = 0
    if social_dict:
        for key, value in social_dict.items():
            if value.get("registered"):
                result += 1
        return result


def get_datetime_or_none(datetime_obj: datetime) -> str:
    """
    Converts datetime object to string and gets datetime string, if not datetime_obj returns None

    :param datetime_obj: datetime
    :return: str: datetime string
    """
    if datetime_obj:
        return datetime_obj.strftime("%Y-%m-%d")
