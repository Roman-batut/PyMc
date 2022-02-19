'''IMPORTS'''

#Imports MultiProcessing
import multiprocessing, random

#Imports Minecraft
from mcstatus import MinecraftServer


'''MAIN'''

serverNames = ["jawfish", "aarwolf", "onager", "locust", "oryxantilopen", "eurasianblackbird", "turtle", "littlebrownbustard"]

#Minecraft
def search(serverName, begin, stop) :
    
    for j in range(begin, stop) :
        number = str(j).zfill(3)
        
        serverMc = str(serverName) + ".aternos.host:42" + number
        
        try :
            server = MinecraftServer.lookup(serverMc)
            status = server.status()
            print("IP :", serverMc)
        except :
            pass

#MultiProcessing
if __name__ == "__main__":
    
    #Nom des Serveurs
    serverName = str(serverNames[random.randint(0, len(serverNames)-1)])
    print("Nom de domaine : " + serverName)

    #Creats processes
    p1 = multiprocessing.Process(target=search, args=(serverName, 0, 125 ))
    p2 = multiprocessing.Process(target=search, args=(serverName, 125, 250 ))
    p3 = multiprocessing.Process(target=search, args=(serverName, 250, 375 ))
    p4 = multiprocessing.Process(target=search, args=(serverName, 375, 500 ))
    p5 = multiprocessing.Process(target=search, args=(serverName, 500, 625 ))
    p6 = multiprocessing.Process(target=search, args=(serverName, 625, 750 ))
    p7 = multiprocessing.Process(target=search, args=(serverName, 750, 875 ))
    p8 = multiprocessing.Process(target=search, args=(serverName, 875, 999 ))

    #Starts processes
    p1.start() ; p2.start() ; p3.start() ; p4.start()
    p5.start() ; p6.start() ; p7.start() ; p8.start()
  
    #Wait until processes are finished
    p1.join() ; p2.join() ; p3.join() ; p4.join()
    p5.join() ; p6.join() ; p7.join() ; p8.join()