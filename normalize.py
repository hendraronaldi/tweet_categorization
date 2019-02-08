import pandas as pd
import numpy as np
import requests
import json

def wordNormalize(data):
    url = 'https://api.prosa.ai/v1/normals'
    with open('config.json') as config_file:
        config = json.load(config_file)

    normalizedTweets = []
    for tweet in data.tweet:
        body = {
            'text': tweet
        }
        response = requests.post(
            url = url,
            data = json.dumps(body),
            headers = config
        )
        normalizedTweets.append(json.loads(response.text)['text'])

    data['tweet'] = normalizedTweets
    return data