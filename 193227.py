import time
import random
import threading
import queue
Nombrefilosofos = ['Aristóteles','Arquímedes','Perictione','Tales de Mileto','Platón']  #Nombre de los filosofos
queue = queue.Queue(maxsize=len(Nombrefilosofos))  #Número entero que establece el límite superior del número de elementos que pueden ser colocados en la cola
posicComieron = [] #Para saber si el numero random ya se eligio

class filosofo():
    def apetito():  
        cont2 = 0
        while cont2 < len(Nombrefilosofos):  #Para que termine hasta que el contador sea menor a la cantidad que hay de filosofos
            cont2 = cont2 + 1
            flag = True 
            while flag:  #Si la posicion que genera el random no se repite, termina
                item = random.randint(0,len(Nombrefilosofos)-1) #Numero random 
                if not item in posicComieron:       #Para saber si el numero random no existe en las posiciones que ya comieron
                    posicComieron.append(item)      #Si no existe se agrega
                    flag = False                    #Para que termine el ciclo while
            queue.put(item)                         #Pone el item  en la cola

    def comer():
        cont = 0
        while cont < len(Nombrefilosofos):   #Para que termine hasta que el contador sea menor a la cantidad que hay de filosofos
            item = queue.get()                  #Se obtiene el dato 
            cont = cont + 1
            time.sleep(random.randint(2,3))  #Tiempo que se queda en sleep antes de comer
            print("=======================================================")
            print("Filosofo",Nombrefilosofos[item], " esta comiendo")  
            time.sleep(random.randint(3,4))  #Tiempo que se queda en sleep, para despues terminar de comer
            print("Filosofo ", Nombrefilosofos[item]," termina de comer")
            print("========================================================")
            queue.task_done()   #le dice a la cola que el procesamiento de la tarea está completo

def main():
    filosofo()
    threading_filosofo = threading.Thread(target=filosofo.apetito)
    threading_comer = threading.Thread(target=filosofo.comer)
    threading_filosofo.start()
    threading_comer.start()

if __name__ == "__main__":
    main()
   