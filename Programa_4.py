from tkinter import *                     # Importa todos los módulos de tkinter / Imports all modules from tkinter
from tkinter import messagebox             # Importa el módulo messagebox para mostrar alertas / Imports messagebox for alerts
from tkinter import ttk                    # Importa ttk para usar widgets avanzados como Treeview / Imports ttk for advanced widgets like Treeview
from Validacion_p4 import Validar          # Importa la clase Validar desde el archivo Validacion_p4 / Imports Validar class from Validacion_p4
import numpy as np                         # Importa numpy (no se usa directamente) / Imports numpy (not directly used)
import random                              # Importa el módulo random para generar números aleatorios / Imports random to generate random numbers
class Principal():                         # Define la clase Principal / Defines the Principal class
    def __init__(self):                    # Constructor de la clase / Class constructor
        self.val = Validar()               # Crea un objeto de la clase Validar / Creates an instance of Validar class
        self.ven = Tk()                    # Crea la ventana principal / Creates the main window
        self.ven.title('Practica 4')       # Asigna el título a la ventana / Sets the window title
        #self.ven.geometry("500x300")      # Línea comentada para establecer tamaño / Commented line to set window size
        ancho = 500                        # Define el ancho de la ventana / Defines window width
        alto = 300                         # Define el alto de la ventana / Defines window height
        ventana_alto = self.ven.winfo_screenwidth()     # Obtiene el ancho de la pantalla / Gets screen width
        ventana_ancho = self.ven.winfo_screenheight()   # Obtiene la altura de la pantalla / Gets screen height
        x = (ventana_alto // 2) - (ancho // 2)          # Calcula la posición X centrada / Calculates centered X position
        y = (ventana_ancho // 2) - (alto // 2)          # Calcula la posición Y centrada / Calculates centered Y position
        self.ven.geometry(f"{ancho}x{alto}+{x}+{y-100}") # Establece tamaño y posición / Sets window size and position
        self.cont = 0                      # Contador para generar claves únicas / Counter for generating unique keys
        self.bandera = False               # Bandera para modo edición / Flag for edit mode
        self.renglon = -1                  # Variable para almacenar fila seleccionada / Variable to store selected row
        self.index = ""                    # Índice temporal para la clave / Temporary key index
    def validarCaja(self):                 # Método para seleccionar y cargar datos desde la tabla / Method to select and load data from table
        self.renglon = self.tabla.selection()   # Obtiene la fila seleccionada / Gets selected row
        if not self.renglon:               # Si no hay selección / If no selection
            messagebox.showerror("Error","Elige una fila")  # Muestra error / Shows error message
        else:
            valores = self.tabla.item(self.renglon, "values")   # Obtiene los valores de la fila / Gets row values
            #valores = self.tabla.item(self.renglon)            # Línea comentada / Commented line
            print(valores)                     # Imprime valores (para depuración) / Prints values (for debugging)
            self.index = valores[0]            # Toma la clave / Gets the key
            self.index = self.index[:len(self.index)-2] # Elimina los últimos dos caracteres / Removes last two characters
            print(self.index)                  # Muestra índice ajustado / Displays adjusted index
            self.nombre.insert(0,valores[1])   # Inserta el nombre en el campo / Inserts name into field
            self.edad.insert(0,valores[3])     # Inserta la edad / Inserts age
            self.correo.insert(0,valores[2])   # Inserta el correo / Inserts email
            self.bandera= True                 # Activa modo edición / Activates edit mode
    def agregarElemento(self):             # Método para agregar o editar elementos / Method to add or edit elements
        if(len(self.nombre.get())==0 or len(self.edad.get())== 0 or len(self.correo.get())== 0):
            messagebox.showerror("Error","Faltan datos")  # Muestra error si faltan datos / Shows error if any field is empty
        else:
            if (self.val.ValidarNombre(self.nombre.get())):    # Valida el nombre usando clase Validar / Validates name using Validar class
                nombre = self.nombre.get()      # Guarda nombre / Stores name
                edad = self.edad.get()          # Guarda edad / Stores age
                correo = self.correo.get()      # Guarda correo / Stores email
                if self.bandera == False:       # Si no está en modo edición / If not in edit mode
                    self.cont += 1              # Incrementa contador / Increments counter
                    clave = str(self.cont)+str(random.randint(1,100))+self.nombre.get()[0:2].upper()  # Genera clave / Generates key
                    self.tabla.insert("","end",values=(clave,nombre,correo,edad)) # Inserta en la tabla / Inserts into table
                    self.nombre.delete(0,END)   # Limpia campo nombre / Clears name field
                    self.edad.delete(0,END)     # Limpia campo edad / Clears age field
                    self.correo.delete(0,END)   # Limpia campo correo / Clears email field
                else:                           # Si está en modo edición / If in edit mode
                    clave = self.index+self.nombre.get()[0:2].upper()  # Regenera clave / Regenerates key
                    print("Modo edicion activado")                      # Mensaje de depuración / Debug message
                    self.tabla.item(self.renglon, values=(clave,nombre,correo,edad)) # Actualiza fila / Updates selected row
                    self.nombre.delete(0,END)
                    self.edad.delete(0,END)
                    self.correo.delete(0,END)
                    self.bandera = False        # Desactiva modo edición / Turns off edit mode
                    self.renglon= -1            # Reinicia selección / Resets row selection
                    messagebox.showinfo("Correcto","Datos Actualizados") # Mensaje de éxito / Success message
            else:
                messagebox.showinfo("Incorrecto","El nombre no es correcto")  # Error de validación / Validation error
    def eliminar(self):                    # Método para eliminar una fila / Method to delete a row
        renglon = self.tabla.selection()   # Obtiene fila seleccionada / Gets selected row
        if not renglon:                    # Si no hay selección / If none selected
            messagebox.showerror("Error","Elige una fila")  # Muestra error / Shows error
        else:
            self.tabla.delete(renglon)     # Elimina fila / Deletes row
            messagebox.showinfo("Correcto","Fila eliminada") # Muestra mensaje / Shows confirmation
    def inicio(self):                      # Método para crear los elementos de la interfaz / Method to build the interface
        Label(self.ven, text="Nombre").place(x=10,y=10)   # Etiqueta Nombre / Name label
        self.nombre = Entry(self.ven, fg="blue")          # Campo de entrada nombre / Entry field for name
        self.nombre.place(x=10, y=40, width=100)
        Label(self.ven, text="Edad").place(x=130,y=10)    # Etiqueta Edad / Age label
        self.edad = Entry(self.ven, fg="green")           # Campo de entrada edad / Entry field for age
        self.edad.place(x=125, y=40, width=100)
        Label(self.ven, text="Correo").place(x=250,y=10)  # Etiqueta Correo / Email label
        self.correo = Entry(self.ven, fg="purple")        # Campo de entrada correo / Entry field for email
        self.correo.place(x=240, y=40, width=100)
        # Botones de acción / Action buttons
        Button(self.ven, text="Agregar", command=self.agregarElemento, width=10).place(x=380,y=50, width=100,height=30)
        Button(self.ven, text="Eliminar", command=self.eliminar, width=10).place(x=380,y=90, width=100,height=30)
        Button(self.ven, text="Selecionar", command=self.validarCaja, width=10).place(x=380,y=130, width=100,height=30)
        # Tabla de datos / Data table
        columnas = ("Clave","Nombre","Correo","Edad")     # Nombres de columnas / Column names
        self.tabla = ttk.Treeview(self.ven, columns= columnas, show="headings")  # Crea tabla / Creates table
        self.tabla.place(x=10, y=100, width=350,height=190)
        for col in columnas:                              # Recorre columnas / Iterates over columns
            self.tabla.heading(col,text=col)               # Asigna encabezado / Sets heading
            self.tabla.column(col, anchor="center", width=30)  # Centra texto / Centers text
        # Barras de desplazamiento / Scrollbars
        scrolly = ttk.Scrollbar(self.ven,orient="vertical", command=self.tabla.yview)   # Scroll vertical / Vertical scroll
        scrollx = ttk.Scrollbar(self.ven, orient="horizontal", command=self.tabla.xview) # Scroll horizontal / Horizontal scroll
        scrolly.place(x=360,y=90,height=200)
        scrollx.place(x=10,y=280, width=350)
        self.ven.mainloop()                 # Inicia el bucle principal / Starts main loop
if __name__=='__main__':                   # Punto de entrada del programa / Program entry point
    app = Principal()                      # Crea objeto Principal / Creates Principal object
    app.inicio()                           # Inicia la interfaz / Starts interface