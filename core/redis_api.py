import redis


class RedisApi:
    """
    Class for working with redis
    """
    def __init__(self):
        self.redis_session = redis.StrictRedis(host='localhost', port=6379, db=5)

    def clear_db(self) -> bool:
        """
        Cleared redis db

        :return: bool
        """

        self.redis_session.flushdb()
        return True

    def get_len_queue(self) -> int:
        """
        Returns count of queue celery

        :return: int
        """
        return self.redis_session.llen("email_checker")


redis_api = RedisApi()

if __name__ == '__main__':
    print(redis_api.get_len_queue())
