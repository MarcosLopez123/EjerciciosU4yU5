import re #libreria de expresiones regulares

path = "Ejercicio.txt"

try:
    archivo = open(path,'r')
except:
    print ("El archivo que intentaste abrir no existe")
    quit()

texto=""

for linea in archivo:
    texto += linea
print(texto)

#Ejercicio 2
patron = r"(\b[0-9]{1,}\.\b[0-9]{1,}|\b[0-9]{1,}\b)"
result = re.findall(patron,texto)

print ("\n Enteros y decimales ", result)


#Ejercicio 3

patron = r"\+|-|/|\*|\=|%"
result = re.findall(patron,texto)
print ("\n Operadores aritméticos encontrados: ", result)


#Ejercicio 4

patron = r"(\>|\<|\>\=|\<\=|\=\=|\!\=)"
result = re.findall(patron,texto)
print ("\n Operadores relacionales encontrados: ", result)


#Ejercicio 5

patron = r"\b(public|static|void|for|while|System|case|import|util|scanner|int|out|System|String|Double)\b"
result = re.findall(patron,texto)
print ("\nPalabras reservadas de JAVA: ", result)