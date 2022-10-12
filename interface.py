from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import prediccion as pr
import cv2 as cv

raiz = Tk()
raiz.title('Test Classifier')
ancho_ventana = 600
alto_ventana = 300

x_ventana = raiz.winfo_screenwidth() // 2 - ancho_ventana // 2
y_ventana = raiz.winfo_screenheight() // 2 - alto_ventana // 2

posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
raiz.geometry(posicion)


def openFile(file):
    global image
    global clase
    global porcentaje
    frame = LabelFrame(raiz, text = 'Image')
    frame.place(relx=0.02, rely = 0.02, relheight = 0.83, relwidth = 0.6)
    image = ImageTk.PhotoImage(Image.open(file).resize((210,210)))
    label = Label(frame, image = image)
    label.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)
    clase, porcentaje = pr.predict(file)
    label2.config(text ='-' + clase)
    label3 = Label(frame2, text = '-' + porcentaje + '%')
    label3.place(relx = 0, rely = 0.6)

def openFolder():
    file = filedialog.askopenfilename(
        title = "File to Open", 
        initialdir = 'img\prueba',
        filetypes = [("Images Files","*.jpg")])
    openFile(file)

def camara():
    cam = cv.VideoCapture(0)
    ret, frame = cam.read()
    cv.imwrite("img\picture.jpg", frame)
    cam.release()
    file = "img/picture.jpg"
    openFile(file)

frame = LabelFrame(raiz, text = 'Image')
frame.place(relx=0.02, rely = 0.02, relheight = 0.83, relwidth = 0.6)
boton = Button(raiz, text = "Open File",command = openFolder)
boton.place(relx = 0.03, rely = 0.87, relwidth = 0.17, relheight = 0.1)
boton = Button(raiz, text = "Open Cam",command = camara)
boton.place(relx = 0.22, rely = 0.87, relwidth = 0.17, relheight = 0.1)

frame2 = LabelFrame(raiz, text = 'Classification')
frame2.place(relx = 0.7, rely = 0.02, relheight = 0.83, relwidth = 0.25)
label_clases = Label(frame2, text = 'Clase')
label_presicion = Label(frame2, text = 'Presicion')
label_clases.place(relx = 0,rely = 0.1)
label_presicion.place(relx = 0,rely = 0.5)
label2 = Label(frame2, text = '')
label2.place(relx = 0, rely = 0.2)

raiz.mainloop()