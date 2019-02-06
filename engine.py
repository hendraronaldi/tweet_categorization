import requests
import json

def wordNormalize(body):
    url = 'https://api.prosa.ai/v1/normals'
    with open('config.json') as config_file:
        config = json.load(config_file)

    response = requests.post(
        url = url,
        data = json.dumps(body),
        headers = config
    )
    return json.loads(response.text)

# Dummy text
body = {
    'text': 'ya mungkin karena perempuan bj merah yg paling kelihatan karena berada di depan, laki2 jg sering jadi bahan joke RK'
}

response = wordNormalize(body)
print(response['text'])