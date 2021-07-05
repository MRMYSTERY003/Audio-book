import pyttsx3 as py
import PyPDF2

en = py.init()
vo = en.getProperty('voices')
en.setProperty('voice',vo[2].id)
en.setProperty('rate', 175)

def speak(text):
    en.say(text)
    en.runAndWait()

book = open('Rich-Dad-Poor-Dad-eBook.pdf','rb')
reader = PyPDF2.PdfFileReader(book)
pages = reader.numPages
speak('the pdf contains '+str(pages)+' pages in it')

for i in range(9, pages):
    page = reader.getPage(i)
    text = page.extractText()
    print(text)
    speak(text)



