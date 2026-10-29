

try:
    archi = open("tony.txt", "w")
    archi.write("Gran Malo FC")
    
except:
    print("Upsss, no se pudo crear el archivo :(")
finally:
    archi.close()