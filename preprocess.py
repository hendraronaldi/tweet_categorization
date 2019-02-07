from normalize import wordNormalize
import numpy as np

# TODO: Add all pre process data in this function
def preProcess(data):
    if len(list(data) > 1):
        data = reshapeColumn(data)
        data = selectImportantColumnOnly(data)
        data = removeMissingValue(data)
    cleaned_data = removeUneccessaryCharactersAndWords(data)
    cleaned_data = wordNormalize(cleaned_data)
    return cleaned_data

def reshapeColumn(data):
    label = ['Keluhan', 'Respon', 'Default']
    data['Label'] = [label[np.where(data.loc[i, ['Keluhan', 'Respon', 'Bukan Keluhan/Respon']].values == 'Ya')[0][0]]
                 if len(np.where(data.loc[i, ['Keluhan', 'Respon', 'Bukan Keluhan/Respon']].values == 'Ya')[0]) > 0
                 else 'None'
                 for i in range(len(data))]
    return data

def selectImportantColumnOnly(data):
    return data[['Tweet', 'Label']]

def removeMissingValue(data):
    return data[data.Label != 'None']

def removeUneccessaryCharactersAndWords(data):
    tweets = data.Tweet
    cleaned_tweets = []
    for tweet in tweets:
        words = [word for word in tweet.split(' ') if (len(word) > 0 and word[0] != '@' and word[0] != '#' and word[0:2] != 'RT' and word[0:4] != 'http')]
        cleaned_tweets.append(' '.join(words))
    data.Tweet = cleaned_tweets
    return data