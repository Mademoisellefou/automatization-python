import pyttsx3,PyPDF2

pdfreader = PyPDF2.PdfFileReader(open('sample.pdf','rb'))
speaker = pyttsx3.init()

for page_num in range(pdfreader.numPages):
    text = pdfreader.getPage(page_num).extractText() ## extracting text from the PDF
    cleaned_text = text.strip().replace('\n',' ')
    print(cleaned_text)
    speaker.save_to_file(cleaned_text,'story.mp3')
    speaker.runAndWait()
speaker.stop()

