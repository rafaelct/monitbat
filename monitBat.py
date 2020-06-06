import win32com.client as wincl
import psutil
import time
#from win10toast import ToastNotifier
import win10toast

toast = win10toast.ToastNotifier()
speak = wincl.Dispatch("SAPI.SpVoice")

minuto = 5
bateria : int
fonte : bool

while True :
    
    try :
        bateria = psutil.sensors_battery().percent
        fonte = psutil.sensors_battery().power_plugged
    except AttributeError :
        print("Não foi encontrado um sensor de bateria.");
        exit(1)


    msgBateria = "Bateria está "+ str(bateria)+" por cento carregada."
    
    if fonte == True :
        msgFonte = "Conectado em uma fonte de energia."
    else :
        msgFonte = "Conectado na bateria."

    if bateria <= 25 and fonte == False :
        minuto = 1
    else :
        minuto = 5
 
    if bateria == 100 and fonte == True :
        minuto = 1
    else :
        minuto = 5
    
    speak.Speak(msgBateria)    
    speak.Speak(msgFonte)

    toast.show_toast("MonitBat",msgBateria+"\n"+msgFonte,duration=20)    

    time.sleep(60*minuto)