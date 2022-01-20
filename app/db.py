# app/db.py

from .repositories import TweetRepository

tweet_repository = TweetRepository()

from .models import Tweet
tweet_repository.add(Tweet("a first tweet"))
tweet_repository.add(Tweet("a second tweet"))