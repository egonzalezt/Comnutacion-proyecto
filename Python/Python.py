from tkinter import * #Importamos tkinter para nuestra interfáz gráfica
import socket #Importamos la librería socket para poder comunicarnos con nuestro ESP8266
import threading #Importamos la libreria multihilo


#Variables para el padding(Espaciado entre objetos) en X e Y
padX=10  
padY=20

ESP_IP = '192.168.0.110'  #IP de nuestro modulo
ESP_PORT = 8266 #Puerto que hemos configurado para que abra el ESP

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Creamos el objeto socket para conectarnos.

root = Tk() #Creamos la ventana principal de nuestra aplicación
root.title("Proyecto Final") #Cambiamos el título a nuestra ventana

B1 = StringVar()
B2 = StringVar()
B3 = StringVar()
T = StringVar()
H = StringVar()

datos = {'B1': B1, 'B2': B2, 'B3': B3, 'T': T, 'H':H}

frame = Frame (root)  #Creamos el contenedor denuestros objetos

lbl_titulo = Label(frame, text="Proyecto Conmutacion")  #Creamos texto para el título
imagenESP = PhotoImage(file="logo.png") #Cargamos imágen del ESP8266
lbl_imagen = Label(frame, image=imagenESP) #Creamos etiqueta para poner la foto del ESP8266

lbl_titulo.grid(row=0, column=0, pady=padY,padx=padX)  #Añadimos el título a nuestro contenedor
lbl_imagen.grid (row=0, column=1,columnspan=2,pady=padY,padx=padX) #Añadimos nuestra imágen al contenedor

''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''

lbl_LEDControl = Label (frame, text="LED1") #Texto "Control LED"
lbl_LEDControl.grid (row=1, column=0) # Añadimos el texto "Control LED" al contenedor

lb2_LEDControl = Label (frame, text="LED2") #Texto "Control LED"
lb2_LEDControl.grid (row=2, column=0) # Añadimos el texto "Control LED" al contenedor

lb3_LEDControl = Label (frame, text="LED3") #Texto "Control LED"
lb3_LEDControl.grid (row=3, column=0) # Añadimos el texto "Control LED" al contenedor

def enciendeLED1():              #Función para encender el LED
    print("Encendiendo LED1")
    dato = '1'
    s.send(dato.encode(encoding='utf_8'))  #Enviamos 1 al modulo ESP
    

def apagaLED1():                #Función para apagar el LED
    print("Apagando LED1")
    dato = '6'
    s.send(dato.encode(encoding='utf_8'))  #Enviamos 0 al modulo ESP

def enciendeLED2():              #Función para encender el LED
    print("Encendiendo LED2")
    dato = '3'
    s.send(dato.encode(encoding='utf_8'))  #Enviamos 1 al modulo ESP

def apagaLED2():                #Función para apagar el LED
    print("Apagando LED2")
    dato = '2'
    s.send(dato.encode(encoding='utf_8'))  #Enviamos 0 al modulo ESP
    
def enciendeLED3():              #Función para encender el LED
    print("Encendiendo LED3")
    dato = '5'
    s.send(dato.encode(encoding='utf_8'))  #Enviamos 1 al modulo ESP

def apagaLED3():                #Función para apagar el LED
    print("Apagando LED3")
    dato = '4'
    s.send(dato.encode(encoding='utf_8'))  #Enviamos 0 al modulo ESP    
    
btn_LEDOn = Button(frame, text="On", fg="green", command=enciendeLED1)  #Creamos botón de encendido del LED
btn_LEDOff = Button(frame, text="Off", fg="red",command=apagaLED1)      #Creamos botón de apagado del LED  
btn_LEDOn.grid (row=1, column=1,pady=padY)      #Añadimos el botónd "ON" a nuestro contenedor.                                                 
btn_LEDOff.grid (row=1, column=2,pady=padY)     #Añadimos el botónd "OFF" a nuestro contenedor. 

btn2_LEDOn = Button(frame, text="On", fg="green", command=enciendeLED2)  #Creamos botón de encendido del LED
btn2_LEDOff = Button(frame, text="Off", fg="red",command=apagaLED2)      #Creamos botón de apagado del LED  
btn2_LEDOn.grid (row=2, column=1,pady=padY)      #Añadimos el botónd "ON" a nuestro contenedor.                                                 
btn2_LEDOff.grid (row=2, column=2,pady=padY)     #Añadimos el botónd "OFF" a nuestro contenedor. 

btn3_LEDOn = Button(frame, text="On", fg="green", command=enciendeLED3)  #Creamos botón de encendido del LED
btn3_LEDOff = Button(frame, text="Off", fg="red",command=apagaLED3)      #Creamos botón de apagado del LED  
btn3_LEDOn.grid (row=3, column=1,pady=padY)      #Añadimos el botónd "ON" a nuestro contenedor.                                                 
btn3_LEDOff.grid (row=3, column=2,pady=padY)     #Añadimos el botónd "OFF" a nuestro contenedor. 

''''''''''''''''''''''''''''''''''''''''''''
''''''''''''''''''''''''''''''''''''''''''''

lbl_B1 = Label(frame, textvariable = B1) #creamos una etiqueta para el boton 1
lbl_B2 = Label(frame, textvariable = B2) #creamos una etiqueda para el boton 2
lbl_B3 = Label(frame, textvariable = B3) #creamos una etiqueda para el boton 2

lbl_B1.grid(row=4, column=0,padx = padX, pady = padY)#Añadimos etiquedas al contenedor
lbl_B2.grid(row=4, column=1,padx = padX, pady = padY)
lbl_B3.grid(row=4, column=2,padx = padX, pady = padY)

lbl_T = Label(frame, textvariable = T) #creamos una etiqueda para el boton 2
lbl_H = Label(frame, textvariable = H) #creamos una etiqueda para el boton 2

lbl_T.grid(row=5, column=0,padx = padX, pady = padY)
lbl_H.grid(row=5, column=1,padx = padX, pady = padY)


frame.pack()


s.connect((ESP_IP , ESP_PORT)) #Nos conectamos a la IP y el puerto que hemos declarado al inicio.


def recibeDatos():

    while True:
        cadena = s.recv(1024)#Recibimios una candena de datos
        print("cadena-> ",cadena)
        lineas = cadena.splitlines() #dividimos la cadena en lineas
        for linea in lineas:
            print(linea)
            dato = linea.split() #Dividimos la cadena en lineas
            datos[dato[0].decode()].set(dato[0].decode()+" "+dato[1].decode())#Actualizamos el diccionario                       
    
hiloRecepcion = threading.Thread(target = recibeDatos)#Creamos un hilo para la recepcion de datos
hiloRecepcion.start()#Iniciamos el hilo para la recepcion de datos


'''

def RGB(int):  
    
    Data = "a" + str(slider.get())    
    Data +=","
    Data +=str(slider1.get())
    Data +=","
    Data +=str(slider2.get())
    
    s.send((Data).encode())

    
slider = Scale(root, from_=0, to=255, orient=HORIZONTAL,command=RGB,length=200, label="RED")   #Creamos un dial para recoger datos numericos
    
slider1 = Scale(root, from_=0, to=255, orient=HORIZONTAL,command=RGB,length=200,label="GREEN")   #Creamos un dial para recoger datos numericos
    
slider2 = Scale(root, from_=0, to=255, orient=HORIZONTAL,command=RGB,length=200,label="BLUE")   #Creamos un dial para recoger datos numericos

slider.pack()
slider1.pack()
slider2.pack()
'''

root.mainloop()


