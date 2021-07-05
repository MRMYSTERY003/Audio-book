''' audio book by 
    Mr_Mystery
    do subscribe my yt channel link in readme file 
'''



import pyttsx3 as py            #importing the modules
import PyPDF2

                                #initilizing the speak engine
en = py.init()
vo = en.getProperty('voices')
en.setProperty('voice',vo[1].id)
en.setProperty('rate', 175)

                                #creating a finction for speaking the text
def speak(text):
    en.say(text)
    en.runAndWait()

                                #opening the pdf in read in binary mode
book = open('Rich-Dad-Poor-Dad-eBook.pdf','rb')
reader = PyPDF2.PdfFileReader(book)             
pages = reader.numPages             #getting tht total number of pages
speak('the pdf contains '+str(pages)+' pages in it')

                                # itrating through all the pages and calling the speak function
for i in range(9, pages):
    page = reader.getPage(i)
    text = page.extractText()
    print(text)
    speak(text)



