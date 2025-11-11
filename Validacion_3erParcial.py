class validar():                                 # ES: Define la clase 'validar' / EN: Defines the 'validar' class
    def __init__(self):                          # ES: Constructor de la clase / EN: Class constructor
        self.con = 0                             # ES: Inicializa un contador en 0 / EN: Initializes a counter at 0
    
    def validarnumeros(self, num):               # ES: Método para validar si una cadena contiene solo números / EN: Method to check if a string contains only numbers
        if  self.con >= len(num):                # ES: Si el contador alcanza la longitud, todos son válidos / EN: If counter reaches length, all chars are valid
            self.con = 0                         # ES: Reinicia el contador / EN: Resets the counter
            return True                          # ES: Retorna verdadero / EN: Returns True
        if ord(num[self.con]) >= 47 and ord(num[self.con]) <=58:   # ES: Verifica si el carácter es número (usando código ASCII) / EN: Checks if character is a number (via ASCII)
            self.con +=1                         # ES: Incrementa el contador / EN: Increments the counter
            return self.validarnumeros(num)       # ES: Llama recursivamente al método / EN: Recursively calls the method
        else:
            self.con = 0                         # ES: Reinicia el contador si hay error / EN: Resets counter if invalid character
            return False                         # ES: Retorna falso / EN: Returns False

    def ValidarLetras(self,dato):                # ES: Valida si una cadena empieza con mayúscula / EN: Validates if a string starts with uppercase letter
        if ord(dato[0]) >= 65 and ord(dato[0]) <=90:   # ES: Verifica si el primer carácter es letra mayúscula (A-Z) / EN: Checks if first char is uppercase letter (A-Z)
            self.con +=1                         # ES: Aumenta el contador / EN: Increases the counter
            return self.validarnumeros(dato)      # ES: Llama al método para validar números / EN: Calls method to validate numbers
        else:
            self.con = 0                         # ES: Reinicia contador si no cumple / EN: Resets counter if invalid
            return False                         # ES: Retorna falso / EN: Returns False

    def ValidarEntrada(self,dato):               # ES: Valida la longitud del dato / EN: Validates input length
        if dato == "":                           # ES: Si está vacío, retorna falso / EN: If empty, returns False
            return False
        if len(dato) == 2:                       # ES: Si tiene dos caracteres, retorna verdadero / EN: If it has two characters, returns True
            return True
        else:
            return False                         # ES: Si no tiene dos, retorna falso / EN: Otherwise, returns False

