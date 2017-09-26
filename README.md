# Cloak

Supports [feature toggling](http://martinfowler.com/bliki/FeatureToggle.html) and ramping features via a lightweight Redis backend. Forked from [feature-ramp](https://github.com/venmo/feature_ramp) for maintenance purposes.

## Installation

Clone the [Cloak repository] locally and install via pip from the local filesystem:

------------------
``` python
$ pip install -f cloak
```

Cloak requires a running Redis server. If your application is written in Python, we recommend using [redis-py](https://github.com/andymccurdy/redis-py) for a convenient way to interface with Redis. To install Redis, follow the [Redis Quick Start](http://redis.io/topics/quickstart).

Once you have redis-py and a Redis server running, you're ready to start using Cloak.

NOTE: Feature Ramp assumes your Redis server is running at localhost on port 6379 (this is the default redis-py configuration). To customize this, make the necessary edits [here](https://github.com/wisr/cloak/blob/master/cloak/__init__.py#L3).

Getting Started
-----------------
``` python
>>> from cloak.feature import Feature
>>> feature_a = Feature('feature_a')
>>> feature_a.activate()
>>> feature_a.is_active
True
>>> feature_a.deactivate()
>>> feature_a.is_active
False
```
