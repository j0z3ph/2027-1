
def cont(n):
    print(n)
    return cont(n+1)

try:
    print(1/1)
    
except:
    print("Tontito, no se puede dividir entre 0")
   
finally:
    print("Fin")