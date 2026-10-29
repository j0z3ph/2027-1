

def cont(a):
    print(a)
    return cont(a + 1)
try:
    print(1/1)
except:
    print("Tontito, no se puede dividir entre 0 jeje")
finally:
    print("Adios")