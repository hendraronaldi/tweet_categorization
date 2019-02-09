# TODO: Add feature extraction
import pickle

def featureExtraction(data):
    #input
    data.columns = ['tweet']
    
    inputTweet = []
    i = 0
    for twt in data.iterrows():
        #unicode error handling
        inputTweet.append(data['tweet'][i].encode('utf-8',errors='ignore'))
        i = i + 1
    
    #load vectorizer
    vectorizer = pickle.load(open('vectorizer.pk','rb'), encoding='latin1')
    
    #transform input data into vector
    x = vectorizer.transform(inputTweet)
    
    return x.toarray()