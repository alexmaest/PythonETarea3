print("")
print("Bienvenido")

print("")
print("Ejercicio 1")
Code = "contraseña"
Pass = input("Ingrese la Contraseña: ")
if Code == Pass.lower():
    print("La Contaseña coincide con la guardada en la variable")
else:
    print("La Contaseña no coincide con la guardada en la variable")


print("")
print("Ejercicio 2")
Nombre = input("Ingrese su nombre: ")
Genero = input("Ingrese su sexo(H o M): ")

if Genero == "M":
    if Nombre.lower()<"m":
        Grupo = "A"
    else:
        Grupo = "B"
else:
    if Nombre.lower()>"m":
        Grupo = "A"
    else:
        Grupo = "B"
print("Tu grupo es " + Grupo)