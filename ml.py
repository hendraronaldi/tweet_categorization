import pandas as pd
import numpy as np
from normalize import wordNormalize

# Example
data = pd.read_excel("../Ica_Labelled Tweets (selesai).xlsx", index_col=None, sheet_name='tweets_text', skiprows=[0,1,2], na_values=['-', ' '])
label = ['Keluhan', 'Respon', 'Default']
data['Label'] = [label[np.where(data.loc[i, ['Keluhan', 'Respon', 'Bukan Keluhan/Respon']].values == 'Ya')[0][0]]
                 if len(np.where(data.loc[i, ['Keluhan', 'Respon', 'Bukan Keluhan/Respon']].values == 'Ya')[0]) > 0
                 else 'None'
                 for i in range(len(data))]
cleaned_data = data[data.Label != 'None']
cleaned_data = cleaned_data[['Tweet', 'Label']]
tweets = cleaned_data.Tweet
cleaned_tweets = []
for tweet in tweets:
    words = [word for word in tweet.split(' ') if (len(word) > 0 and word[0] != '@' and word[0] != '#' and word[0:2] != 'RT' and word[0:4] != 'http')]
    cleaned_tweets.append(' '.join(words))
cleaned_data['Tweet'] = cleaned_tweets
normalized_tweets = wordNormalize(cleaned_data.head())
print(normalized_tweets)