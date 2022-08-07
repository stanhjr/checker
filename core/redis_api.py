import redis


class RedisApi:
    def __init__(self):
        self.redis_session = redis.StrictRedis(host='localhost', port=6379, db=0)

    def clear_db(self):
        self.redis_session.flushdb()
        return True

    def get_len_queue(self):
        return self.redis_session.llen("email_checker")


redis_api = RedisApi()

if __name__ == '__main__':
    print(redis_api.get_len_queue())
