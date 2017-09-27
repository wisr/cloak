redis = None


def initialize(conn):
    global redis

    if not conn:
        raise ValueError("Must provide a redis connection")

    redis = conn
