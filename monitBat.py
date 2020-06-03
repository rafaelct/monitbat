import win32com.client as wincl
import psutil
import time
#from win10toast import ToastNotifier
import win10toast

toast = win10toast.ToastNotifier()
speak = wincl.Dispatch("SAPI.SpVoice")
minuto = 5

while True :
    
    bateria = psutil.sensors_battery().percent
    fonte = psutil.sensors_battery().power_plugged

    if bateria <= 25 and fonte == False :
        minuto = 1
    else :
        minuto = 5
 
    if bateria == 100 and fonte == True :
        minuto = 1
    else :
        minuto = 5
    
    speak.Speak("Bateria está "+ str(bateria)+" por cento carregada.")
    
    if fonte == True :
        speak.Speak("Conectado em uma fonte de energia.")
        toast.show_toast("MonitBat","Bateria está "+ str(bateria)+" por cento carregada.\nConectado em uma fonte de energia.",duration=20)    
    else :
        speak.Speak("Conectado na bateria.")
        toast.show_toast("MonitBat","Bateria está "+ str(bateria)+" por cento carregada.\nConectado na bateria.",duration=20)

    time.sleep(60*minuto)