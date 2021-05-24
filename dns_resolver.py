#!/urs/bin/python

import socket
import sys

arquivo = open("subdominios_dns_resolver.txt", "r")
url = sys.argv[1]

for linha in arquivo:
    #print(linha)
    subdominio = (linha[0 : (len(linha)-1)]+""+url)
    
    try:
        ip = socket.gethostbyname(subdominio)
        print(subdominio+" ---> "+ip)
    except:
        continue 
arquivo.close()
