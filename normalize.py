import pandas as pd
import numpy as np
import requests
import json

def wordNormalize(data):
    url = 'https://api.prosa.ai/v1/normals'
    with open('../config.json') as config_file:
        config = json.load(config_file)

    normalizedTweets = []
    for tweet in data.Tweet:
        body = {
            'text': tweet
        }
        response = requests.post(
            url = url,
            data = json.dumps(body),
            headers = config
        )
        normalizedTweets.append(json.loads(response.text)['text'])

    data['Tweet'] = normalizedTweets

    # Optional: save result
    # data.to_csv("database/normalized_tweets.csv", index=False)
    return data