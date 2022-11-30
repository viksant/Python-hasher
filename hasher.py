import os
import hashlib, signal, pdb, sys, base64, time, os.path

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
    print("1) MD5")
    print("2) SHA1")
    print("3) SHA224")
    print("4) SHA256")
    print("5) SHA384")
    print("6) SHA2-512")
    print("7) Salir")

def select_option(option):
    if option == 1:
        file = input("Ingresa el archivo: ")
        while not os.path.exists(file):
            print("El archivo no existe, ingrese uno valido porfavor")
            file = input("Ingresa el archivo: ")

        if os.path.isfile(file):
            hash_select()
            election = int(input("Elige un hash:"))
            if election == 1:
                with open(file, "r") as f:
                    for line in f:
                        line = line.strip()
                        print(line + " -> " + hashlib.md5(line.encode()).hexdigest())
            elif election == 2:
                with open(file, "r") as f:
                    for line in f:
                        line = line.strip()
                        print(line + " -> " + hashlib.sha1(line.encode()).hexdigest())
            elif election == 3:
                with open(file, "r") as f:
                    for line in f:
                        line = line.strip()
                        print(line + " -> " + hashlib.sha224(line.encode()).hexdigest())
            elif election == 4:
                with open(file, "r") as f:
                    for line in f:
                        line = line.strip()
                        print(line + " -> " + hashlib.sha256(line.encode()).hexdigest())
            elif election == 5:
                with open(file, "r") as f:
                    for line in f:
                        line = line.strip()
                        print(line + " -> " + hashlib.sha384(line.encode()).hexdigest())
            elif election == 6:
                with open(file, "r") as f:
                    for line in f:
                        line = line.strip()
                        print(line + " -> " + hashlib.sha512(line.encode()).hexdigest())
            elif election == 7:
                sys.exit(1)
        else:
            print("El archivo no existe")
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
            sys.exit(1)
        else:
            print("Opcion invalida")
            sys.exit(1)

    elif option == 3:
        guardado_archivo=int(input("¿Desea guardar el resultado en un archivo? 1-Si 2-No: "))
        hash_select()

        if guardado_archivo == 1:
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
                    sys.exit(1)

        else:
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
                sys.exit(1)
            else:
                print("Opcion invalida")
                sys.exit(1)

    elif option == 4:
        sys.exit(1)

if __name__ == "__main__":
    select_option(option)
    #codigo