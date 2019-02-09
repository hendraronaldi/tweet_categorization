from normalize import wordNormalize
import numpy as np
import pandas as pd
import re, string

# TODO: Add all pre process data in this function
def preProcess(data):
    # input dataframe
    if len(list(data))> 1: # if train data
        data = reshapeColumn(data)
        data = selectImportantColumnOnly(data)
        data = removeMissingValue(data)
    cleaned_data = removeUneccessaryCharactersAndWords(data)
    cleaned_data = wordNormalize(cleaned_data)
    return cleaned_data # output dataframe

# reshape target label into 1 column
def reshapeColumn(data):
    # input dataframe
    label = ['Keluhan', 'Respon', 'Lain-lain']
    data['Label'] = [label[np.where(data.loc[i, ['Keluhan', 'Respon', 'Bukan Keluhan/Respon']].values == 'Ya')[0][0]]
                 if len(np.where(data.loc[i, ['Keluhan', 'Respon', 'Bukan Keluhan/Respon']].values == 'Ya')[0]) > 0
                 else 'None'
                 for i in range(len(data))]
    data.columns = map(str.lower, data.columns)
    return data # output dataframe

# get dataframe contains tweet and label column only
def selectImportantColumnOnly(data):
    # input dataframe
    return data[['tweet', 'label']] # output dataframe

# remove rows with no label
def removeMissingValue(data):
    # input dataframe
    return data[data.label != 'None'] # output dataframe

# get words from tweets
def removeUneccessaryCharactersAndWords(data):
    # input dataframe
    regex = re.compile('[%s]' % re.escape(string.punctuation))
    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           "]+", flags=re.UNICODE)

    tweets = data.tweet
    cleaned_tweets = []
    for tweet in tweets:
        words = [emoji_pattern.sub(r'', regex.sub('', word)) for word in tweet.split(' ') if (len(word) > 0 and not word.startswith('@') and not word.startswith('#') and not word.startswith('RT') and not word.startswith('http'))]
        cleaned_tweets.append(' '.join(words))
    data.tweet = cleaned_tweets
    return data # output dataframe