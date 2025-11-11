from tkinter import*                      # Importa todos los módulos de tkinter / Imports all modules from tkinter
from tkinter import messagebox             # Importa el módulo messagebox para mostrar mensajes / Imports messagebox module to show messages


class Principal():                         # Define la clase Principal / Defines the Principal class
    def __init__(self):                    # Constructor de la clase / Class constructor
        #self.val = validar()              # Línea comentada, podría ser para validación / Commented line, possibly for validation
        self.ven = Tk()                    # Crea la ventana principal / Creates the main window
        #self.ven.geometry("300x200")      # Línea comentada que fija el tamaño de la ventana / Commented line to set window size
        self.lis = []                      # Crea una lista vacía / Creates an empty list
        ancho = 350                        # Ancho de la ventana / Window width
        alto = 250                         # Alto de la ventana / Window height
        ventana_alto = self.ven.winfo_screenwidth()    # Obtiene el ancho de pantalla / Gets screen width
        ventana_ancho = self.ven.winfo_screenwidth()   # Obtiene el ancho de pantalla (duplicado) / Gets screen width (duplicated)
        x = (ventana_alto // 2) - (ancho // 2)         # Calcula la posición X centrada / Calculates centered X position
        y = (ventana_ancho // 2) - (alto //2)          # Calcula la posición Y centrada / Calculates centered Y position
        self.ven.geometry(f"{ancho}x{alto}+{x+50}+{y-300}")  # Define tamaño y posición / Sets window size and position
        self.ven.title('Practica 3')       # Establece el título de la ventana / Sets the window title
    def quitar_placeholder1(self, event):  # Elimina placeholder del campo Nombre / Removes placeholder from Name field
        if self.Nombre.get() == self.placeholder1:      # Si el texto es igual al placeholder / If text equals placeholder
            self.Nombre.delete(0, END)    # Borra el texto actual / Deletes current text
            self.Nombre.config(fg="black") # Cambia color de texto a negro / Changes text color to black
    def quitar_placeholder2(self, event):  # Elimina placeholder del campo Teléfono / Removes placeholder from Phone field
        if self.Telefono.get() == self.placeholder2:    
            self.Telefono.delete(0, END)  # Borra el texto actual / Deletes current text
            self.Telefono.config(fg="black") # Cambia color a negro / Changes color to black
    def quitar_placeholder3(self, event):  # Elimina placeholder del campo Domicilio / Removes placeholder from Address field
        if self.Domicilio.get() == self.placeholder3:
            self.Domicilio.delete(0, END)  # Borra el texto actual / Deletes current text
            self.Domicilio.config(fg="black") # Cambia color a negro / Changes color to black
    def poner_placeholder1(self, event):   # Restaura placeholder del campo Nombre / Restores placeholder for Name field
        if self.Nombre.get() == "":
            self.Nombre.insert(0, self.placeholder1)    # Inserta el texto placeholder / Inserts placeholder text
            self.Nombre.config(fg="gray")  # Cambia el color a gris / Changes color to gray
    def poner_placeholder2(self, event):   # Restaura placeholder del campo Teléfono / Restores placeholder for Phone field
        if self.Telefono.get() == "":
            self.Telefono.insert(0, self.placeholder2)
            self.Telefono.config(fg="gray")
    def poner_placeholder3(self, event):   # Restaura placeholder del campo Domicilio / Restores placeholder for Address field
        if self.Domicilio.get() == "":
            self.Domicilio.insert(0, self.placeholder3)
            self.Domicilio.config(fg="gray")
    def inicio(self):                      # Función para inicializar la interfaz / Function to initialize the interface
        # Campo de texto para Nombre / Text field for Name
        self.placeholder1 = "Nombre"      
        self.Nombre = Entry(self.ven, fg="gray")   # Crea campo de entrada / Creates entry field
        self.Nombre.insert(0, self.placeholder1)   # Inserta texto por defecto / Inserts default text
        self.Nombre.bind("<FocusIn>", self.quitar_placeholder1) # Evento al enfocar / On focus event
        self.Nombre.bind("<FocusOut>", self.poner_placeholder1) # Evento al perder foco / On focus out event
        #self.Nombre.bind("<Return>", self.validarCaja)          # Línea comentada / Commented line
        self.Nombre.place(x=10, y=10, width=100)   # Posiciona el campo / Positions the field
        # Campo de texto para Teléfono / Text field for Phone
        self.placeholder2 = "Telefono"
        self.Telefono = Entry(self.ven, fg="gray")
        self.Telefono.insert(0, self.placeholder2)
        self.Telefono.bind("<FocusIn>", self.quitar_placeholder2)
        self.Telefono.bind("<FocusOut>", self.poner_placeholder2)
        #self.Telefono.bind("<Return>", self.validarCaja)
        self.Telefono.place(x=120, y=10, width=100)
        # Campo de texto para Domicilio / Text field for Address
        self.placeholder3 = "Domicilio"
        self.Domicilio = Entry(self.ven, fg="gray")
        self.Domicilio.insert(0, self.placeholder3)
        self.Domicilio.bind("<FocusIn>", self.quitar_placeholder3)
        self.Domicilio.bind("<FocusOut>", self.poner_placeholder3)
        self.Domicilio.bind("<Return>", self.validarCaja)  # Valida al presionar Enter / Validates on Enter
        self.Domicilio.place(x=230, y=10, width=100)
        Label(self.ven, text='Sexo').place(x=10, y=30)  # Etiqueta de texto / Text label
        self.modo = StringVar(value='F')               # Variable para radio buttons / Variable for radio buttons
        Radiobutton(self.ven, text="F", variable=self.modo, value="F").place(x=10, y=50) # Botón femenino / Female button
        Radiobutton(self.ven, text="M", variable=self.modo, value="M").place(x=10, y=70) # Botón masculino / Male button
        self.lista = Listbox(self.ven, heig=7, width=40, bg="White")  # Lista para mostrar datos / Listbox to show data
        self.lista.place(x=10, y=100)
        Button(self.ven, text='Agregar', command=self.agregar).place(x=250, y=150)  # Botón Agregar / Add button
        self.ven.mainloop()                     # Inicia el bucle principal / Starts main event loop
    def agregar(self):                          # Método vacío por ahora / Empty method for now
        pass
    def validarCaja(self, event):               # Valida los campos de texto / Validates text fields
        if (self.Nombre.get() == self.placeholder1 or self.Telefono.get() == self.placeholder2
            or self.Domicilio == self.placeholder3 or self.Domicilio.get() == ""):
            messagebox.showerror('Error','Faltan datos')   # Muestra error si faltan datos / Shows error if data missing
        else:
            nombre = self.Nombre.get()          # Obtiene nombre / Gets name
            telefono = self.Telefono.get()      # Obtiene teléfono / Gets phone
            domicilio = self.Domicilio.get()    # Obtiene domicilio / Gets address
            if self.modo.get() == "F":
                sexo = "Femenino"               # Define sexo femenino / Defines female gender
            else:
                sexo = "Masculino"              # Define sexo masculino / Defines male gender
            clave = nombre[0] + telefono[0] + domicilio[2:]  # Crea clave única / Creates unique key
            persona = clave + " _" + nombre + " _ " + telefono + " _ " + domicilio + " _ " + sexo
            self.lista.insert(END, persona)     # Inserta persona en la lista / Inserts person in list
if __name__=='__main__':                        # Punto de entrada del programa / Program entry point
    app = Principal()                           # Crea objeto Principal / Creates Principal object
    app.inicio()                                # Inicia la aplicación / Starts the application

