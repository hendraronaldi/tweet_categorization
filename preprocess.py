from normalize import wordNormalize

# TODO: Add all pre process data in this function
def preProcess(data):
    cleaned_data = wordNormalize(data)
    return cleaned_data