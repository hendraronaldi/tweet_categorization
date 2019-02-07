from normalize import wordNormalize
import numpy as np

# TODO: Add all pre process data in this function
def preProcess(data):
    # input dataframe
    if len(list(data) > 1): # if train data
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
    return data # output dataframe

# get dataframe contains tweet and label column only
def selectImportantColumnOnly(data):
    # input dataframe
    return data[['Tweet', 'Label']] # output dataframe

# remove rows with no label
def removeMissingValue(data):
    # input dataframe
    return data[data.Label != 'None'] # output dataframe

# get words from tweets
def removeUneccessaryCharactersAndWords(data):
    # input dataframe
    tweets = data.Tweet
    cleaned_tweets = []
    for tweet in tweets:
        words = [word for word in tweet.split(' ') if (len(word) > 0 and word[0] != '@' and word[0] != '#' and word[0:2] != 'RT' and word[0:4] != 'http')]
        cleaned_tweets.append(' '.join(words))
    data.Tweet = cleaned_tweets
    return data # output dataframe