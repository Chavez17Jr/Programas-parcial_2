class Validar():                            # Define la clase Validar / Defines the Validar class
    def __init__(self):                     # Constructor de la clase / Class constructor
        self.con = 0                        # Contador interno usado en validaciones / Internal counter used for validations
    def ValidarNumeros(self, num):          # Valida que una cadena contenga solo números / Validates that a string contains only numbers
        if self.con >= len(num):            # Si se recorrió toda la cadena / If entire string has been checked
            self.con = 0                    # Reinicia el contador / Resets counter
            return True                     # Retorna verdadero / Returns True
        
        if ord(num[self.con]) >= 47 and ord(num[self.con]) <= 58:  # Comprueba si el carácter es numérico (0–9) / Checks if character is numeric (0–9)
            self.con += 1                   # Avanza al siguiente carácter / Moves to next character
            return self.ValidarNumeros(num) # Llama recursivamente al método / Recursively calls the method
        else:
            self.con = 0                    # Reinicia el contador / Resets counter
            return False                    # Retorna falso si hay un carácter no numérico / Returns False if a non-numeric character is found
    def ValidarLetra(self, dato):           # Valida que el primer carácter sea una letra mayúscula / Validates that the first character is uppercase
        if ord(dato[0]) >= 65 and ord(dato[0])<= 90:   # Verifica rango de letras A-Z / Checks A-Z ASCII range
            return True                     # Si está en el rango, es válido / If in range, it’s valid
        else:
            return False                    # Si no, no es válido / Otherwise, not valid
    def ValidarEntradas(self, dato):        # Valida la longitud de la entrada / Validates the length of the input
        if dato == "":                      # Si está vacío / If empty
            return False                    # Retorna falso / Returns False
        if len(dato) == 2:                  # Si tiene exactamente 2 caracteres / If it has exactly 2 characters
            return True                     # Retorna verdadero / Returns True
        else:
            return False                    # En cualquier otro caso, falso / Otherwise, False
    def ValidarNombre(self, nom):           # Valida que el nombre contenga solo letras o espacios / Validates that name contains only letters or spaces
        c = 0                               # Contador de caracteres válidos / Counter for valid characters
        for i in nom:                       # Recorre cada carácter del nombre / Loops through each character in the name
            if (ord(i) >= 97 and ord(i) <= 122) or (ord(i) >= 97 and ord(i) <= 122) or (ord(i)==32):  
                c += 1                      # Si es letra o espacio, suma 1 / If letter or space, increment count
        if c == len(nom):                   # Si todos los caracteres son válidos / If all characters are valid
            return True                     # Retorna verdadero / Returns True
        else:
            return False                    # Retorna falso si hay caracteres inválidos / Returns False if any invalid characters