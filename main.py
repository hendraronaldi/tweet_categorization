from tkinter import *
from tkinter import filedialog
import pandas as pd

from preprocess import preProcess
from ml import predictInput

def submit():
    inputData = {
        'Tweet': txtInput.get()
    }
    data = pd.DataFrame(data=inputData)
    # cleaned_data = preProcess(data)
    # result = predictInput(cleaned_data)
    # lblOutput.configure(text=str(result))

def uploadAction(event=None):
    filename = filedialog.askopenfilename()
    if not filename.endswith(".csv") and not filename.endswith(".xlsx"):
        lblOutput.configure(text="Wrong input file")
    else:
        # TODO: Read input file and process
        if filename.endswith(".xlsx"):
            data = pd.read_excel(filename) 
        else:
            data = pd.read_csv(filename)

        # cleaned_data = preProcess(data)
        # result = predictInput(cleaned_data)
        # lblOutput.configure(text=str(result))

if __name__ == "__main__":
    window = Tk()
    window.title("Klasifikasi Keluhan")
    window.geometry('350x200')

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