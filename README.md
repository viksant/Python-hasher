# Python hash generator & cracker

The project is still under development and I am aware that it can be optimized, new options can be added, etc. Therefore, I will update the repository as I implement significant changes.
If you have an idea that you think may be interesting or any suggestions, I will be happy to read them. Discord: 𝑉𝐼𝐾𝑆𝐴𝑁𝑇#4536

## Spanish

#### Hash Generator
Para ejecutar el script , simplemente usamos el siguiente comando:
python3 <script> e introducimos los datos que se nos vayan pidiendo.

#### Hash Cracker
Al igual que en el caso anterior, pero esta vez le tenemos que pasar 3 parámetros:
-m <mode> en formato texto, como por ejemplo md5
-c "hash" incluyendo las comillas dobles
-w <wordlist>

Ejemplo de ejecución:
python3 hash_cracker.py -m md5 -c "hash..." -w rockyou.txt

## English

#### Hash Generator
To run the script, we simply use the following command:
python3 <script> 
and enter the requested data.

#### Hash Cracker
As in the previous case, but this time we have to pass 3 parameters:
-m <mode> in text format, such as md5.
-c "hash" including double quotes
-w <wordlist>
Example of execution:
python3 hash_cracker.py -m md5 -c "hash..." -w rockyou.txt




