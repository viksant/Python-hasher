import os
import hashlib, signal, pdb, sys, base64

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

def select_option(option):
    if option == 1:
        file = input("Ingresa el archivo: ")
        print("1) MD5")
        print("2) SHA1")
        print("3) SHA224")
        print("4) SHA256")
        print("5) SHA384")
        print("6) SHA2-512")
        print("7) Salir")
        eleccion = int(input("Elige un hash:"))
        if eleccion == 1:
            with open(file, "r") as f:
                for line in f:
                    line = line.strip()
                    print(line + " -> " + hashlib.md5(line.encode()).hexdigest())
        elif eleccion == 2:
            with open(file, "r") as f:
                for line in f:
                    line = line.strip()
                    print(line + " -> " + hashlib.sha1(line.encode()).hexdigest())
        elif eleccion == 3:
            with open(file, "r") as f:
                for line in f:
                    line = line.strip()
                    print(line + " -> " + hashlib.sha224(line.encode()).hexdigest())
        elif eleccion == 4:
            with open(file, "r") as f:
                for line in f:
                    line = line.strip()
                    print(line + " -> " + hashlib.sha256(line.encode()).hexdigest())
        elif eleccion == 5:
            with open(file, "r") as f:
                for line in f:
                    line = line.strip()
                    print(line + " -> " + hashlib.sha384(line.encode()).hexdigest())
        elif eleccion == 6:
            with open(file, "r") as f:
                for line in f:
                    line = line.strip()
                    print(line + " -> " + hashlib.sha512(line.encode()).hexdigest())
        elif eleccion == 7:
            sys.exit(1)

    elif option == 2:
        print("1) MD5")
        print("2) SHA1")
        print("3) SHA224")
        print("4) SHA256")
        print("5) SHA384")
        print("6) SHA2-512")
        print("7) Salir")
        eleccion = int(input("Elige un hash:"))

        if eleccion == 1:
            string = input("Ingresa el string: ")
            print("El hash es: " + hashlib.md5(string.encode()).hexdigest())
        elif eleccion == 2:
            string = input("Ingresa el string: ")
            print("El hash es: " + hashlib.sha1(string.encode()).hexdigest())
        elif eleccion == 3:
            string = input("Ingresa el string: ")
            print("El hash es: " + hashlib.sha224(string.encode()).hexdigest())
        elif eleccion == 4:
            string = input("Ingresa el string: ")
            print("El hash es: " + hashlib.sha256(string.encode()).hexdigest())
        elif eleccion == 5:
            string = input("Ingresa el string: ")
            print("El hash es: " + hashlib.sha384(string.encode()).hexdigest())
        elif eleccion == 6:
            string = input("Ingresa el string: ")
            print("El hash es: " + hashlib.sha512(string.encode()).hexdigest())
        elif eleccion == 7:
            sys.exit(1)

    elif option == 3:
        print("1) MD5")
        print("2) SHA1")
        print("3) SHA224")
        print("4) SHA256")
        print("5) SHA384")
        print("6) SHA2-512")
        print("7) Salir")
        eleccion = int(input("Elige un hash:"))

        list = []
        n = int(input("Ingresa el numero de palabras: "))
        for i in range(0, n):
            print("Ingresa la palabra", i + 1, ":")
            item = input()
            list.append(item)

        if eleccion == 1:
            for i in list:
                print(i + " -> " + hashlib.md5(i.encode()).hexdigest())
        elif eleccion == 2:
            for i in list:
                print(i + " -> " + hashlib.sha1(i.encode()).hexdigest())
        elif eleccion == 3:
            for i in list:
                print(i + " -> " + hashlib.sha224(i.encode()).hexdigest())
        elif eleccion == 4:
            for i in list:
                print(i + " -> " + hashlib.sha256(i.encode()).hexdigest())
        elif eleccion == 5:
            for i in list:
                print(i + " -> " + hashlib.sha384(i.encode()).hexdigest())
        elif eleccion == 6:
            for i in list:
                print(i + " -> " + hashlib.sha512(i.encode()).hexdigest())
        elif eleccion == 7:
            sys.exit(1)


if __name__ == "__main__":
    select_option(option)
