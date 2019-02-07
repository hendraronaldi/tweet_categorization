# TODO: Add feature extraction
import os.path
import pickle

def featureExtraction(data):
    data.columns = ['tweet']
    
    inputTweet = []
    i = 0
    for twt in data.iterrows():
        #buang white space, simpan dalam list
        inputTweet.append(unicode(data['tweet'][i],errors='ignore'))
        i = i + 1
    
    vectorizer = pickle.load(open('vectorizer.pk','rb'))
    x = vectorizer.transform(inputTweet)
    
    return x