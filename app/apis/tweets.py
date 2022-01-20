# app/apis/tweets.py
# pylint: disable=missing-docstring

from flask_restx import Namespace, Resource, fields
from app.db import tweet_repository
from flask import jsonify

api = Namespace('tweets')

model = api.model('Model', {
    'id': fields.Integer,
    'text': fields.String,
    'created_at': fields.DateTime,
})

@api.route('/<int:id>')
@api.response(404, 'Tweet not found')
class TweetResource(Resource):
    @api.marshal_with(model)
    def get(self, id):
        tweet = tweet_repository.get(id)
        
        if tweet is None:
            api.abort(404)
        else:
            return tweet