'''Hacer un programa que lea nombre, apellido paterno y materno en 3 cajas separadas
ademas, leer dia, mes y año en 3 cajas separadas.
Al precionar un boton se agregara a un listbox el RFC de la persona, ademas, contrendra 2
botones para eliminar elementos de listbox mediante pilas y colas'''
'''Primer letra y vocal del apeido paterno, primer letra del apeido materno, primer letra del nombre
todo mayusculas, año (2) mes (2) dia (2)'''
from tkinter import *                            # ES: Importa todas las funciones de tkinter / EN: Imports all functions from tkinter
from tkinter import messagebox                   # ES: Importa los cuadros de mensajes / EN: Imports message boxes
class Principal():                               # ES: Define la clase Principal / EN: Defines the Principal class
    def __init__(self):                          # ES: Constructor de la clase / EN: Class constructor
        self.ventana = Tk()                      # ES: Crea la ventana principal / EN: Creates the main window
        ancho = 550                              # ES: Define el ancho de la ventana / EN: Sets the window width
        alto = 230                               # ES: Define la altura de la ventana / EN: Sets the window height
        ventana_alto = self.ventana.winfo_screenmmwidth()   # ES: Obtiene el ancho de la pantalla en milímetros (probablemente debería ser pixels) / EN: Gets screen width in millimeters (should likely be pixels)
        ventana_ancho = self.ventana.winfo_screenmmheight() # ES: Obtiene la altura de la pantalla en milímetros / EN: Gets screen height in millimeters
        x = (ventana_alto // 2) - (ancho // 2)   # ES: Calcula posición X centrada / EN: Calculates centered X position
        y = (ventana_ancho // 2) - (alto // 2)   # ES: Calcula posición Y centrada / EN: Calculates centered Y position
        self.ventana.geometry(f"{ancho}x{alto}+{x+500}+{y+250}")  # ES: Define tamaño y posición de la ventana / EN: Sets window size and position
        self.lista = []                          # ES: Inicializa lista vacía para guardar RFCs / EN: Initializes empty list to store RFCs
        self.con = 0                             # ES: Inicializa contador / EN: Initializes counter
    def Inicio(self):                            # ES: Crea los elementos gráficos de la interfaz / EN: Creates the GUI elements
        # Caja de texto / Text boxes
        self.nombre = Entry(self.ventana)        # ES: Campo de texto para nombre / EN: Text field for first name
        self.nombre.place(x=30,y=30)             
        self.apellidoP = Entry(self.ventana)     # ES: Campo de texto para apellido paterno / EN: Text field for last name (paternal)
        self.apellidoP.place(x=160,y=30)
        self.apellidoM = Entry(self.ventana)     # ES: Campo de texto para apellido materno / EN: Text field for maternal last name
        self.apellidoM.place(x=290,y=30)
        self.dia = Entry(self.ventana)           # ES: Campo de texto para día de nacimiento / EN: Text field for birth day
        self.dia.place(x=30,y=90)
        self.mes = Entry(self.ventana)           # ES: Campo de texto para mes de nacimiento / EN: Text field for birth month
        self.mes.place(x=160,y=90)
        self.anio = Entry(self.ventana)          # ES: Campo de texto para año de nacimiento / EN: Text field for birth year
        self.anio.place(x=290,y=90)
        # ListBox
        self.listaBox = Listbox(self.ventana, height=13, width=20, bg='white', activestyle="dotbox", fg="Black")  
        # ES: Lista visual para mostrar los RFC generados / EN: Visual list to display generated RFCs
        self.listaBox.place(x=420, y=10)
        # Botones / Buttons
        Button(self.ventana,text="Agregar",command=self.agregarRFC, height=3, width=10,).place(x=50,y=150)  
        # ES: Botón para agregar RFC / EN: Button to add RFC
        Button(self.ventana,text="Eliminar\n(Pilas)",command=self.eliminarPilas, height=3, width=12,).place(x=175,y=150)  
        # ES: Botón para eliminar con método pila (último en entrar, primero en salir) / EN: Button to delete using stack method (LIFO)
        Button(self.ventana,text="Eliminar\n(Colas)",command=self.eliminarColas, height=3, width=12,).place(x=305,y=150)  
        # ES: Botón para eliminar con método cola (primero en entrar, primero en salir) / EN: Button to delete using queue method (FIFO)        
        # # Labels
        Label(self.ventana, text="Nombre").place(x=40, y=10)             # ES: Etiqueta para nombre / EN: Label for name
        Label(self.ventana, text="Apellido Paterno").place(x=170, y=10)  # ES: Etiqueta para apellido paterno / EN: Label for paternal surname
        Label(self.ventana, text="Apellido Materno").place(x=300, y=10)  # ES: Etiqueta para apellido materno / EN: Label for maternal surname
        Label(self.ventana, text="Dia").place(x=40, y=70)                # ES: Etiqueta para día / EN: Label for day
        Label(self.ventana, text="Mes").place(x=170, y=70)               # ES: Etiqueta para mes / EN: Label for month
        Label(self.ventana, text="Año").place(x=300, y=70)               # ES: Etiqueta para año / EN: Label for year
        # mainloop
        self.ventana.mainloop()                   # ES: Inicia el ciclo principal de la ventana / EN: Starts the main window loop
    def agregarRFC(self):                        # ES: Método para generar y agregar un RFC / EN: Method to generate and add an RFC
        # Validar nombre / Validate name
        if self.nombre.get() == "":
            messagebox.showerror("ERROR", "Escribe un Nombre")   # ES: Error si está vacío / EN: Error if empty
            return
        else:
            if not self.validarLetras(self.nombre.get()):        # ES: Verifica que solo tenga letras / EN: Checks for letters only
                return
        # Validar apellido paterno / Validate paternal surname
        if self.apellidoP.get() == "":
            messagebox.showerror("ERROR", "Escribe el apellido Paterno")
            return
        else:
            if not self.validarLetras(self.apellidoP.get()):
                return
        # Validar apellido materno / Validate maternal surname
        if self.apellidoM.get() == "":
            messagebox.showerror("ERROR", "Escribe el apellido Materno")
            return
        else:
            if not self.validarLetras(self.apellidoM.get()):
                return
        # Validar día / Validate day
        if self.dia.get() == "" or len(self.dia.get()) != 2:
            messagebox.showerror("ERROR", "Escribe un día válido de 2 dígitos")
            return
        else:
            if not self.validarNumeros(self.dia.get()):
                return
        # Validar mes / Validate month
        if self.mes.get() == "" or len(self.mes.get()) != 2:
            messagebox.showerror("ERROR", "Escribe un mes válido de 2 dígitos")
            return
        else:
            if not self.validarNumeros(self.mes.get()):
                return
        # Validar año / Validate year
        if self.anio.get() == "" or len(self.anio.get()) != 4:
            messagebox.showerror("ERROR", "Escribe un año válido de 4 dígitos")
            return
        else:
            if not self.validarNumeros(self.anio.get()):
                return
        # Construir RFC / Build RFC
        self.rfc = ""
        self.rfc = (
            f"{self.apellidoP.get().upper()[:2]}"  # ES: Primeras dos letras del apellido paterno / EN: First two letters of paternal surname
            f"{self.apellidoM.get().upper()[0]}"   # ES: Primera letra del apellido materno / EN: First letter of maternal surname
            f"{self.nombre.get().upper()[0]}"      # ES: Primera letra del nombre / EN: First letter of given name
            f"{self.anio.get()[2:4]}"              # ES: Últimos dos dígitos del año / EN: Last two digits of year
            f"{self.mes.get()}"                    # ES: Mes completo / EN: Full month
            f"{self.dia.get()}"                    # ES: Día completo / EN: Full day
        )
        self.lista.append(self.rfc)                # ES: Agrega RFC a la lista / EN: Adds RFC to internal list
        self.listaBox.insert(self.listaBox.size()+1,self.rfc)  # ES: Muestra RFC en la lista visual / EN: Displays RFC in visual list
        # Limpia los campos / Clears all fields
        self.nombre.delete(0,END)
        self.apellidoM.delete(0,END)
        self.apellidoP.delete(0,END)
        self.dia.delete(0,END)
        self.mes.delete(0,END)
        self.anio.delete(0,END)
    def eliminarPilas(self):                      # ES: Elimina último RFC (modo pila) / EN: Deletes last RFC (stack mode)
        if self.listaBox.size() <= 0:             # ES: Verifica si la lista está vacía / EN: Checks if list is empty
            messagebox.showerror("ERROR", "La lista esta vacia")
            return
        else:
            self.listaBox.delete(self.listaBox.size()-1)  # ES: Elimina último elemento / EN: Deletes last item
    def eliminarColas(self):                      # ES: Elimina primer RFC (modo cola) / EN: Deletes first RFC (queue mode)
        if self.listaBox.size() <= 0:
            messagebox.showerror("ERROR", "La lista esta vacia")
            return
        else:
            self.listaBox.delete(0)
    def validarLetras(self, dato):                # ES: Valida que el dato contenga solo letras / EN: Validates that input contains only letters
        if dato.isalpha():
            return True
        else:
            messagebox.showerror("ERROR", f"( {dato} ) contiene numeros.")  # ES: Muestra error si contiene números / EN: Shows error if it contains numbers
            return False
    def validarNumeros(self, numero):             # ES: Valida que el dato contenga solo números / EN: Validates that input contains only numbers
        if numero.isdigit():
            return True
        else:
            messagebox.showerror("ERROR", f"( {numero} ) contiene letras.") # ES: Muestra error si contiene letras / EN: Shows error if it contains letters
            return False
if __name__=='__main__':                         # ES: Verifica si el archivo se ejecuta directamente / EN: Checks if file is run directly
    app = Principal()                             # ES: Crea una instancia de la clase Principal / EN: Creates an instance of the Principal class
    app.Inicio()                                  # ES: Llama al método para iniciar la interfaz / EN: Calls the method to start the GUI