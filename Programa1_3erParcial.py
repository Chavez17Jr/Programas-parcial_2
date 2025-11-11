from tkinter import*                             # ES: Importa todas las funciones del módulo tkinter / EN: Imports all functions from tkinter module
from tkinter import messagebox                    # ES: Importa la herramienta para mostrar cuadros de mensaje / EN: Imports the messagebox tool for popup messages
from Validacion_3erParcial import validar         # ES: Importa la clase validar desde otro archivo / EN: Imports the 'validar' class from another file
import numpy as np                                # ES: Importa la librería NumPy con el alias np / EN: Imports the NumPy library with alias np  

class Principal():                                # ES: Define la clase Principal / EN: Defines the Principal class
    def __init__(self):                           # ES: Método constructor de la clase / EN: Class constructor method
        self.val = validar()                      # ES: Crea un objeto de la clase validar / EN: Creates an instance of the validar class
        self.ven = Tk()                           # ES: Crea la ventana principal de la aplicación / EN: Creates the main application window
        #self.ven.geometry("300x200")             # ES: (Comentado) Define tamaño de la ventana / EN: (Commented) Sets the window size
        self.lis = []                             # ES: Inicializa una lista vacía / EN: Initializes an empty list
        ancho = 320                               # ES: Define el ancho de la ventana / EN: Sets the window width
        alto = 210                                # ES: Define la altura de la ventana / EN: Sets the window height
        ventana_alto = self.ven.winfo_screenwidth()   # ES: Obtiene el ancho de la pantalla / EN: Gets the screen width
        ventana_ancho = self.ven.winfo_screenwidth()  # ES: Obtiene otra vez el ancho (error, debería ser height) / EN: Gets width again (likely should be height)
        x = (ventana_alto // 2) - (ancho // 2)        # ES: Calcula posición X centrada / EN: Calculates centered X position
        y = (ventana_ancho // 2) - (alto //2)         # ES: Calcula posición Y centrada / EN: Calculates centered Y position
        self.ven.geometry(f"{ancho}x{alto}+{x+50}+{y-300}")  # ES: Define tamaño y posición de la ventana / EN: Sets the window’s size and position

    def validarCaja(self):                        # ES: Valida los datos ingresados en la caja de texto / EN: Validates input from the entry box
        valor = self.dato.get()                   # ES: Obtiene el texto ingresado / EN: Gets the entered text
        # if (self.val.validarnumeros(valor)):    # ES: (Comentado) Valida si es número / EN: (Commented) Checks if it's a number
        #     messagebox.showinfo("Correcto", "Si es un numero")  # ES: Muestra mensaje correcto / EN: Shows success message
        # else:                                   # ES: Si no es número / EN: If not a number
        #     messagebox.showerror("Incorrecto", "No es un numero")  # ES: Muestra mensaje de error / EN: Shows error message
        if (self.val.validarnumeros(valor)):       # ES: Verifica si el valor es numérico / EN: Checks if the value is numeric
            if (self.val.ValidarEntrada(valor)):   # ES: Verifica si cumple con la longitud permitida / EN: Validates allowed input length
                self.lista.insert(self.lista.size()+1,valor)  # ES: Agrega el valor a la lista / EN: Inserts the value into the list
                self.dato.delete(0,END)            # ES: Limpia la caja de texto / EN: Clears the input box
            else: 
                messagebox.showerror("Error", "solo se permiten dos digitos")  # ES: Muestra error si hay más de dos dígitos / EN: Shows error if more than two digits
                self.dato.delete(0,END)             # ES: Limpia la caja de texto / EN: Clears the input box
        else:
            messagebox.showerror("Error", "No son numeros")   # ES: Error si no es número / EN: Error if input is not numeric
            self.dato.delete(0,END)                # ES: Limpia la caja de texto / EN: Clears the input box
        
        #print(f'la cadena tiene{str(self.val.ValidarEntrada(valor))}')   # ES: (Comentado) Muestra validación en consola / EN: (Commented) Prints validation result
        self.label.config(text=f'Numero de elementos en la lista: {str(self.lista.size())}')  # ES: Actualiza etiqueta con el tamaño de la lista / EN: Updates label with list size

    def eliminardato(self):                       # ES: Elimina un elemento de la lista / EN: Deletes an element from the list
        if self.lista.size() <= 0:                # ES: Verifica si la lista está vacía / EN: Checks if list is empty
            messagebox.showerror("Error", "Lista vacia")  # ES: Muestra error si está vacía / EN: Shows error if list is empty
            return                                # ES: Sale del método / EN: Exits the method
        if(self.modo.get()) == 'Pila':            # ES: Si el modo es pila / EN: If mode is stack
            #ultimo que entra es el primero en salir / EN: Last in, first out
            self.lista.delete(self.lista.size()-1) # ES: Elimina el último elemento / EN: Deletes the last element
        else:
            #primero que entra primero que sale / EN: First in, first out
            self.lista.delete(0)                  # ES: Elimina el primer elemento / EN: Deletes the first element
        self.label.config(text=f'Numero de elementos en la lista: {str(self.lista.size())}')  # ES: Actualiza etiqueta / EN: Updates label

    def ordenar(self):                            # ES: Ordena los elementos de la lista / EN: Sorts the elements in the list
        self. lis = list(self.lista.get(0,END))   # ES: Obtiene los datos actuales de la lista / EN: Retrieves current list items
        if len(self.lis) <=0:                     # ES: Verifica si está vacía / EN: Checks if list is empty
            messagebox.showerror('Error','La lista esta vacia')  # ES: Muestra error / EN: Shows error message
        else:
        #     #metodo de seleccion, se usa un auxiliar en 0 para comparar e intercambia posicion
        #     self.arreglo = np.array(self.lis)
        #     # for i in self.arreglo:
        #     #     print(i)}
        #     p = 0
        #     for i in range (0, len(self.lis)):
        #         aux = int(self.lis[i])
        #         p = i
        #         for x in range(i,len(self.lis)):
        #             if aux < int (self.lis[x]):
        #                 aux = int (self.lis[x])
        #                 p = x
        #         self.lis[p] = self.lis[i]
        #         self.lis[i] = str(aux)        
        #     print(self.lis)
        #     self.lista.delete(0,END)
        #     for i in self.lis:
        #         self.lista.insert(self.lista.size()+1,str(i))
            #metodo de burbuja, compara una posicion con otra / EN: Bubble sort method, compares adjacent positions
            for i in range(0,len(self.lis)):      
                for x in range(0,len(self.lis)-1):
                    if self.lis[x]>self.lis[x+1]: # ES: Si el elemento actual es mayor, intercambia / EN: If current item is greater, swap
                        aux = self.lis[x]         # ES: Guarda temporalmente el valor / EN: Temporarily stores the value
                        self.lis[x] = self.lis[x+1]  # ES: Intercambia los valores / EN: Swaps the values
                        self.lis[x+1] = aux       # ES: Completa el intercambio / EN: Completes the swap
            print(self.lis)                       # ES: Muestra la lista ordenada en consola / EN: Prints sorted list in console
            self.lista.delete(0,END)              # ES: Borra todos los elementos actuales / EN: Clears current listbox items
            for i in self.lis:                    # ES: Recorre los elementos ordenados / EN: Loops through sorted elements
                self.lista.insert(self.lista.size()+1,str(i))  # ES: Inserta cada elemento ordenado / EN: Inserts each sorted element

    def inicio(self):                             # ES: Configura la interfaz gráfica / EN: Sets up the graphical interface
        self.dato = Entry(self.ven)               # ES: Caja de texto para ingresar datos / EN: Input box for user data
        self.dato.place(x = 50, y = 10)           # ES: Posición de la caja / EN: Entry position
        self.modo = StringVar(value="Pila")       # ES: Variable para modo (Pila o Cola) / EN: Variable for mode (Stack or Queue)
        Radiobutton(self.ven, text="Pila",variable=self.modo,value="Pila").place(x=50,y=40)  # ES: Botón de modo pila / EN: Stack mode button
        Radiobutton(self.ven, text="Colas",variable=self.modo,value="Colas").place(x=100,y=40) # ES: Botón de modo cola / EN: Queue mode button
        Button(self.ven, text="Validar", command=self.validarCaja).place(x = 100, y = 90)     # ES: Botón para validar entrada / EN: Button to validate input
        Button(self.ven, text="Eliminar", command=self.eliminardato).place(x = 100, y = 120)  # ES: Botón para eliminar elemento / EN: Button to delete element
        Button(self.ven, text="Ordendar", command=self.ordenar).place(x = 100, y = 150)       # ES: Botón para ordenar / EN: Button to sort list
        self.label = Label(text="Numero")         # ES: Etiqueta de texto / EN: Text label
        self.label.place(x=10, y=60)              # ES: Posición de la etiqueta / EN: Label position
        self.lista = Listbox(self.ven, heig =10, width= 10, bg = "White")  # ES: Lista visual / EN: Visual listbox
        self.lista.place (x= 210, y= 20)          # ES: Posición de la lista / EN: Listbox position
        self.ven.mainloop()                       # ES: Inicia el bucle principal de la ventana / EN: Starts the main GUI loop

if __name__=='__main__':                         # ES: Verifica si se ejecuta directamente / EN: Checks if script runs directly
    app = Principal()                             # ES: Crea objeto de la clase Principal / EN: Creates an instance of Principal
    app.inicio()                                  # ES: Llama al método inicio / EN: Calls the inicio method
