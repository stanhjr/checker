from socialscan.util import Platforms, sync_execute_queries

from core.db.db_api import data_api


def social_media_checker(email: str):
    """
    Checking availability social media and save result to database

    :param email: email to check
    :return:
    """
    queries = [email, ]
    platforms = [Platforms.LASTFM, Platforms.INSTAGRAM, Platforms.SPOTIFY, Platforms.PINTEREST, Platforms.SNAPCHAT,
                 Platforms.TUMBLR]
    results = sync_execute_queries(queries, platforms)
    for result in results:
        if result.available is False:
            if str(result.platform) == 'Lastfm':
                data_api.set_available_last_fm(result.query)
            if str(result.platform) == 'Instagram':
                data_api.set_available_instagram(result.query)
            if str(result.platform) == 'Spotify':
                data_api.set_available_spotify(result.query)
            if str(result.platform) == 'Pinterest':
                data_api.set_available_pinterest(result.query)
            if str(result.platform) == 'Tumblr':
                data_api.set_available_tumblr(result.query)

