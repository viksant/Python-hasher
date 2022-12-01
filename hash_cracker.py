import os, io, getopt, hashlib, sys, os, time, argparse, signal
from pwn import *


def def_handler(sig, frame):
    print("\n\n [!] Saliendo.. ")
    sys.exit(1)

#selection = int(input("\n Elige que desea desencriptar:" + "\n 1) Una palabra" + "\n 2) Un archivo" "\n 3) Salir" + "\n\n Ingresa una opcion: "))

signal.signal(signal.SIGINT, def_handler)

if len(sys.argv) != 7:
    print("Usage: python3 hash_cracker.py -m <mode> -c 'hash' -w <wordlist>")
    sys.exit(1)

parser = argparse.ArgumentParser(description='Hash cracker')
parser.add_argument('-c', '--hash', type=str,  help='Hash to crack', required=True)
parser.add_argument('-w', '--wordlist', type=str, help='Wordlist to use', required=True)
parser.add_argument('-m', '--mode', type=str, help='Hash mode', required=True)
args = parser.parse_args()


def hash_cracker(hash, mode, wordlist):
    with open(args.wordlist, "r", encoding="latin-1") as f:
        if "md5" in args.mode:
            h=hashlib.md5
        elif "sha1" in args.mode:
            h=hashlib.sha1
        elif "sha224" in args.mode:
            h=hashlib.sha224
        elif "sha256" in args.mode:
            h=hashlib.sha256
        elif "sha384" in args.mode:
            h=hashlib.sha384
        elif "sha512" in args.mode:
            h=hashlib.sha512
        else:
            print("Hash mode not supported")
            sys.exit(1)

        for line in f:
            line = line.strip()
            encodeline=str.encode(line)
            lineHash = h(encodeline).hexdigest()
            if lineHash == args.hash:
                with open ("recent", "a+") as f:
                    print("Hash cracked: " + line)
                    f.write(line +":" + args.hash + " (" + args.mode+")" + "\n")
                sys.exit(1)

if __name__ == "__main__":
    hash_cracker(args.hash, args.mode, args.wordlist)