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

def hash_select():
    data = [[1, 'MD5', 0, '8743b52063cd84097a65d1633f5c74f5'],
            [2, 'SHA1', 100, 'b89eaac7e61417341b710b727768294d0e6a277b'],
            [3, 'SHA2-224', 1300, 'e4fa1555ad877bf0ec455483371867200eee89550a93eff2f95a6198'],
            [4, 'SHA2-256', 1400, '127e6fbfe24a750e72930c220a8e138275656b8e5d8f48a98c3c92df2caba935'],
            [5, 'SHA2-384', 10800,'07371af1ca1fca7c6941d2399f3610f1e392c56c6d73fddffe38f18c430a2817028dae1ef09ac683b62148a2c8757f42'],
            [6, 'SHA2-512', 1700,'82a9dda829eb7f8ffe9fbe49e45d47d2dad9664fbb7adf72492e3c81ebd3e29134d9bc12212bf83c6840f10e8246b9db54a4859b7ccd0123d86e5872c1e5082f']]
    print(tabulate(data, headers=["Id", "Hash", "Hash mode", "Example"]))

def file_exists(prompt_str):
    while True:
        filename = input("Ingresa el archivo, si no existe, se repetirá este mensaje: ")
        try:
            if os.path.isfile(filename):
                return filename
        except IOError:
            print("El archivo no existe, ingrese uno valido porfavor")
            continue

def select_option(option):
    if option == 1:
        archivo_existe = file_exists("Ingresa el archivo: ")
        if (archivo_existe):
            hash_select()
            election = int(input("Elige un hash:"))
            if election == 1:
                with open(archivo_existe, "r") as f:
                    for line in f:
                        line = line.strip()
                        print(line + " -> " + hashlib.md5(line.encode()).hexdigest())
            elif election == 2:
                with open(archivo_existe, "r") as f:
                    for line in f:
                        line = line.strip()
                        print(line + " -> " + hashlib.sha1(line.encode()).hexdigest())
            elif election == 3:
                with open(archivo_existe, "r") as f:
                    for line in f:
                        line = line.strip()
                        print(line + " -> " + hashlib.sha224(line.encode()).hexdigest())
            elif election == 4:
                with open(archivo_existe, "r") as f:
                    for line in f:
                        line = line.strip()
                        print(line + " -> " + hashlib.sha256(line.encode()).hexdigest())
            elif election == 5:
                with open(archivo_existe, "r") as f:
                    for line in f:
                        line = line.strip()
                        print(line + " -> " + hashlib.sha384(line.encode()).hexdigest())
            elif election == 6:
                with open(archivo_existe, "r") as f:
                    for line in f:
                        line = line.strip()
                        print(line + " -> " + hashlib.sha512(line.encode()).hexdigest())
            elif election == 7:
                print("Saliendo..")
                sys.exit(1)

    elif option == 2:
        hash_select()
        election = int(input("Elige un hash:"))
        if election == 1:
            string = input("Ingresa el string: ")
            print("El hash es: " + hashlib.md5(string.encode()).hexdigest())
        elif election == 2:
            string = input("Ingresa el string: ")
            print("El hash es: " + hashlib.sha1(string.encode()).hexdigest())
        elif election == 3:
            string = input("Ingresa el string: ")
            print("El hash es: " + hashlib.sha224(string.encode()).hexdigest())
        elif election == 4:
            string = input("Ingresa el string: ")
            print("El hash es: " + hashlib.sha256(string.encode()).hexdigest())
        elif election == 5:
            string = input("Ingresa el string: ")
            print("El hash es: " + hashlib.sha384(string.encode()).hexdigest())
        elif election == 6:
            string = input("Ingresa el string: ")
            print("El hash es: " + hashlib.sha512(string.encode()).hexdigest())
        elif election == 7:
            print("Saliendo..")
            sys.exit(1)
        else:
            print("Opcion invalida")
            sys.exit(1)

    elif option == 3:
        guardado_archivo=int(input("¿Desea guardar el resultado en un archivo? 1-Si 2-No: "))

        if guardado_archivo == 1:
            hash_select()
            election = int(input("Elige un hash:"))
            archivo = input("Ingrese el nombre del archivo de destino: ")
            f = open(archivo, "w")
            list = []
            n = int(input("Ingresa el numero de palabras: "))
            for i in range(0, n):
                print("Ingresa la palabra", i + 1, ":")
                item = input()
                list.append(item)

            for palabra in list:
                if election == 1:
                    f.write(palabra + " -> " + hashlib.md5(palabra.encode()).hexdigest() + "\n")
                elif election == 2:
                    f.write(palabra + " -> " + hashlib.sha1(palabra.encode()).hexdigest() + "\n")
                elif election == 3:
                    f.write(palabra + " -> " + hashlib.sha224(palabra.encode()).hexdigest() + "\n")
                elif election == 4:
                    f.write(palabra + " -> " + hashlib.sha256(palabra.encode()).hexdigest() + "\n")
                elif election == 5:
                    f.write(palabra + " -> " + hashlib.sha384(palabra.encode()).hexdigest() + "\n")
                elif election == 6:
                    f.write(palabra + " -> " + hashlib.sha512(palabra.encode()).hexdigest() + "\n")
                elif election == 7:
                    print("Saliendo..")
                    sys.exit(1)

        else:
            hash_select()
            election = int(input("Elige un hash:"))
            list = []
            n = int(input("Ingresa el numero de palabras: "))
            for i in range(0, n):
                print("Ingresa la palabra", i + 1, ":")
                item = input()
                list.append(item)

            if election == 1:
                for i in list:
                    print(i + " -> " + hashlib.md5(i.encode()).hexdigest())
            elif election == 2:
                for i in list:
                    print(i + " -> " + hashlib.sha1(i.encode()).hexdigest())
            elif election == 3:
                for i in list:
                    print(i + " -> " + hashlib.sha224(i.encode()).hexdigest())
            elif election == 4:
                for i in list:
                    print(i + " -> " + hashlib.sha256(i.encode()).hexdigest())
            elif election == 5:
                for i in list:
                    print(i + " -> " + hashlib.sha384(i.encode()).hexdigest())
            elif election == 6:
                for i in list:
                    print(i + " -> " + hashlib.sha512(i.encode()).hexdigest())
            elif election == 7:
                print("Saliendo..")
                sys.exit(1)
            else:
                print("Opcion invalida")
                sys.exit(1)

    elif option == 4:
        print()
        sys.exit(1)


if __name__ == "__main__":
    select_option(option)