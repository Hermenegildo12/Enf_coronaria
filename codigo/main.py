
from limpieza import presion_farmaco



def main():
    print("Buenos dias")
    ID = input("Introduzca su ID de paciente. (Recuerde de 0 a 302) ID: ")
    x=presion_farmaco(ID)
    print(x)
    
 






if __name__=="__main__":
   main()