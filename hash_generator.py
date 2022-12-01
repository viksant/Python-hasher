import os
import hashlib, signal, pdb, sys, base64, time, os.path
from tabulate import tabulate


def def_handler(sig, frame):
    print("\n\n [!] Saliendo.. ")
    sys.exit(1)


signal.signal(signal.SIGINT, def_handler)


def menu_selector():
    print("1) Hashear un archivo")
    print("2) Hashear una sola palabra")
    print("3) Hashear varias palabras")
    print("4) Salir")
    print("")


menu_selector()
option = int(input("Ingresa una opcion: "))

while option != 1 and option != 2 and option != 3 and option != 4:
    option = int(input("Ingresa una valida: "))


def hash_select():
    data = [[1, 'MD5', 0],
            [2, 'SHA1', 100],
            [3, 'SHA2-224', 1300],
            [4, 'SHA2-256', 1400],
            [5, 'SHA2-384', 10800],
            [6, 'SHA2-512', 1700]]
    print(tabulate(data, headers=["Id", "Hash", "Hash mode"]))


def file_exists(prompt_str):
    while True:
        filename = input("Ingresa el archivo, si no existe, se repetirá este mensaje: ")
        try:
            if os.path.isfile(filename):
                return filename
        except IOError:
            print("El archivo no existe, ingrese uno valido porfavor")
            continue

numero_elegido = {
    1: hashlib.md5,
    2: hashlib.sha1,
    3: hashlib.sha224,
    4: hashlib.sha256,
    5: hashlib.sha384,
    6: hashlib.sha512,
}


def chose_hash(number):
    if number in numero_elegido:
        return numero_elegido[number]


def select_option(option):

    if option == 1:
        archivo_existe = file_exists("Ingresa el archivo: ")
        if (archivo_existe):
            hash_select()
            election = int(input("\n Elige un hash:"))

            while election != 1 and election != 2 and election != 3 and election != 4 and election != 5 and election != 6:
                election = int(input("Id incorrecto. Ingresa un Id válido: "))

            hash = chose_hash(election)

            if election in numero_elegido:
                with open(archivo_existe, "r") as f:
                    for line in f:
                        line = line.strip()
                        encodeline = str.encode(line)
                        lineHash = hash(encodeline).hexdigest()
                        print(line + " -> " + hash(line.encode()).hexdigest())

    elif option == 2:
        hash_select()
        election = int(input("\nElige un hash:"))
        while election != 1 and election != 2 and election != 3 and election != 4 and election != 5 and election != 6:
            election = int(input("Id incorrecto. Ingresa un Id válido: "))

        hash = chose_hash(election)

        if election in numero_elegido:
            palabra = input("Ingresa la palabra: ")
            print(palabra + " -> " + hash(palabra.encode()).hexdigest())
        else:
            print("Opcion invalida")
            sys.exit(1)
    elif option == 3:
        guardado_archivo=int(input("¿Desea guardar el resultado en un archivo? 1-Si 2-No: "))

        if guardado_archivo == 1:
            hash_select()

            election = int(input("\nElige un hash:"))
            while election != 1 and election != 2 and election != 3 and election != 4 and election != 5 and election != 6:
                election = int(input("Id incorrecto. Ingresa un Id válido: "))

            archivo = input("Ingrese el nombre del archivo de destino: ")
            f = open(archivo, "w")

            list = []
            n = int(input("Ingresa el numero de palabras: "))
            for i in range(0, n):
                print("Ingresa la palabra a hashear", i + 1, ":")
                item = input()
                list.append(item)

            for palabra in list:
                hash = chose_hash(election)
                if election in numero_elegido:
                    f.write(palabra + " -> " + hash(palabra.encode()).hexdigest() + "\n")

        else:
            hash_select()
            election = int(input("\nElige un hash:"))
            while election != 1 and election != 2 and election != 3 and election != 4 and election != 5 and election != 6:
                election = int(input("Id incorrecto. Ingresa un Id válido: "))
            list = []
            n = int(input("Ingresa el numero de palabras: "))
            for i in range(0, n):
                print("Ingresa la palabra a hashear", i + 1, ":")
                item = input()
                list.append(item)

            for palabra in list:
                hash = chose_hash(election)
                if election in numero_elegido:
                    print(palabra + " -> " + hash(palabra.encode()).hexdigest())

    elif option == 4:
        print("Saliendo..")
        sys.exit(1)


if __name__ == "__main__":
    select_option(option)
