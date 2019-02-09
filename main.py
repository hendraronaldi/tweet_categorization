# python 3 tkinter
from tkinter import *
from tkinter import filedialog

# python 2 tkinter
# from Tkinter import *
# import Tkinter, Tkconstants, tkFileDialog

import pandas as pd
from preprocess import preProcess
from feature import featureExtraction
from predict import predictInput

def submit():
    inputData = {
        'tweet': [txtInput.get()]
    }
    data = pd.DataFrame(data=inputData)
    cleaned_data = preProcess(data)
    cleaned_data = featureExtraction(cleaned_data)
    result = predictInput(cleaned_data)
    result.insert(loc=0, column='tweet', value=[txtInput.get()])
    lblOutput.configure(text=str(result))

def uploadAction(event=None):
    # python 3 import file using tkinter
    filename = filedialog.askopenfilename()

    # python 2 import file using tkinter
    # filename = tkFileDialog.askopenfilename()

    if not filename.endswith(".csv") and not filename.endswith(".xlsx"):
        lblOutput.configure(text="Wrong input file")
    else:
        # TODO: Read input file and process
        if filename.endswith(".xlsx"):
            data = pd.read_excel(filename) 
        else:
            data = pd.read_csv(filename, encoding = "ISO-8859-1")

        cleaned_data = preProcess(data)
        cleaned_data = featureExtraction(cleaned_data)
        result = predictInput(cleaned_data)
        result.insert(loc=0, column='tweet', value=data['tweet'])
        lblOutput.configure(text=str(result))

if __name__ == "__main__":
    window = Tk()
    window.title("Klasifikasi Keluhan")
    window.geometry('700x550')

    lblInput = Label(window, text="Masukkan text")
    lblInput.grid(column=0, row=0)

    txtInput = Entry(window,width=10)
    txtInput.grid(column=1, row=0)

    btnUpload = Button(window, text="Upload file", command=uploadAction)
    btnUpload.grid(column=2, row=0)

    btnSubmit = Button(window, text="Submit", command=submit)
    btnSubmit.grid(column=0, row=1)

    lblOutput = Label(window, text="")
    lblOutput.grid(column=0, row=2)
    window.mainloop()