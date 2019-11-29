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

#Ejercicio 1

patron = r"[a-zA-Z][\w\d]*"
result1 = re.findall(patron,texto)
#print ("\nVariables: ", result)

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

#Ejercicio 6
a="[\+|\-|\/|\*|\%]"#para concatenar la expresion regular en los ejercicios 
b="[\d+\.\d+|\w]+"
patron = r"(\w+( |)=( |)"+b+")"
result = re.findall(patron,texto)
print ("\nSentencias de Asignacion: ", result)

#Ejercicio 7
patron= r"(\w+( |)=( |)"+b+"( |)"+a+"( |)"+b+")"
result = re.findall(patron,texto)
print ("\nOperaciones aritméticas básicas: ", result)


#Ejercicio 8
patron= r"([ |](\={2,3}|\>|\<|\!|\>=|\<=|\!=)[ |]"+b+")"
result = re.findall(patron,texto)
print ("\nExpresiones booleanas básicas: ", result)

#Ejercicio 9
patron=r'(\w+( |)=( |)[\d+\.\d+|\w]+( |)[\+|\-|\/|\*|\%]( |)[\(\d+\.\d+|\w]+( |)[\+|\-|\/|\*|\%]( |)[\d+\.\d+|\w]+\));'
result = re.findall(patron,texto)
print ("\nFormulas más complejas : ", result)

#Ejercicio 10
patron= r"\b(if|for|while|switch|forEach)\b"
result = re.findall(patron,texto)
print ("\nEl encabezado de estructura de control: ", result)

for i in result1:
    if (i!="import" and i!="int" and i!="double" and i!="float" and i!="static" and i!="public" and i!="void" and i!="for" and i!="System" and i!="while" and i!="case" and i!="Scanner" and i!="util" and i!="String" and i!="println" and i!="java" and i!="class" and i!="main" and i!="args" and i!="out" and i!="if" and i!="else"):
        print("Variables válidas: "+i)