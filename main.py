import pyttsx3
from pdfreader import SimplePDFViewer
from tkinter.filedialog import askopenfilename

book = askopenfilename(filetypes=[("PDF Files", "*.pdf")])

with open(book, "rb") as file:
    viewer = SimplePDFViewer(file)
    player = pyttsx3.init()

    while True:
        try:
            viewer.render()
            text = "".join(viewer.canvas.strings)
            player.say(text)
            player.runAndWait()
            viewer.next()
        except StopIteration:
            break
