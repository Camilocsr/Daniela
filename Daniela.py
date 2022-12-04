import pyttsx3 #convierte de audio a texto....
import speech_recognition as sr # reconocimiento de voz...
import webbrowser # busqueda por la web
import datetime # para tener aacceso a la hora y dia del pc...
import wikipedia # busqueda por wikipedia
import os #abrir aplicaciones del pc
import tkinter as tk #interfas fraficas...
from tkinter import * #inporta todo tekinder entero
from tkinter import ttk #tablas...
  
def takeCommand(): # activar el microfono.
  
    r = sr.Recognizer() 
  
    with sr.Microphone() as source: 
        print('Escuchando...') 
          
        # r.pause_threshold = 0.7
        audio = r.listen(source) 
          
        try: 
            print("Reconocioendo comando...") 
              
            Query = r.recognize_google(audio, language='es-ES') 
            print("El comando es=", Query) 
              
        except Exception as e: 
            print(e) 
            speak("Dilo de nuevo por favor, no te he escuchado bien....") 
            return "None"
          
    return Query #aaa
  
def speak(audio): #activar audio del pc
      
    engine = pyttsx3.init() 
    voices = engine.getProperty('voices') 
    engine.setProperty('voice', voices[5].id) 
    engine.setProperty('rate', 170)
    engine.say(audio)   
    engine.runAndWait()
  
def tellDay(): 
      
    day = datetime.datetime.today().weekday() + 1
      
    Day_dict = {1: 'Lunes', 2: 'Martes',  
                3: 'Miercoles', 4: 'Jueves',  
                5: 'Viernes', 6: 'Sabado', 
                7: 'Domingo'} 
      
    if day in Day_dict.keys(): 
        day_of_the_week = Day_dict[day] 
        print(day_of_the_week) 
        speak("El dia es: " + day_of_the_week) 
  
  
def tellTime(): 
      
    time = str(datetime.datetime.now()) 
      
    print(time) 
    hour = time[11:13] 
    min = time[14:16] 
    speak("El tiempo es: " + hour + "Horas y" + min + "Minutos")     
  
def Hello(): 
      
    speak("Hola soy tu asistente virtual dime en que te puedo ayudar...") 

def interfas(): # interfas grafica...
    window = tk.Tk()
    window.title('Daniela, interfas de comandos...')
    window.resizable(0,0)
    window.iconbitmap('csr.ico')
    # window.config(bg= 'darkmagenta')

    window.tree = ttk.Treeview(height = 12, columns = 1)
    window.tree.grid(row = 0, column = 0, columnspan = 2)
    window.tree.heading('#0', text = 'Comandos', anchor = CENTER)

    window.tree.insert('',END,text='Abrir youtube')
    window.tree.insert('',END,text='Video')
    window.tree.insert('',END,text='abrir codigo')
    window.tree.insert('',END,text='día')
    window.tree.insert('',END,text='comandos')
    window.tree.insert('',END,text='dime la hora')
    window.tree.insert('',END,text='adíos')
    window.tree.insert('',END,text='en wikipedia')
    window.tree.insert('',END,text='dime tu nombre')
    window.tree.insert('',END,text='creador')
    window.tree.insert('',END,text='abrir')

    window.mainloop()

apps = { # libro de apps en el computador...
    'word' : r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE", 
    'powerpoint' : r"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE",
    'Excel' : r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE",
    'torrent' : r"C:\Users\LENOVO\AppData\Roaming\uTorrent\uTorrent.exe",
    'winrar':r'C:\Users\LENOVO\Documents\Camilo Solano Rodriguez\descargas\WinRAR.exe',
    'zoom':r'C:\Users\LENOVO\AppData\Roaming\Zoom\bin\Zoom.exe',
    'Google':r'C:\Program Files\Google\Chrome\Application\chrome.exe',
    'firefox':r'C:\Program Files\Mozilla Firefox\firefox.exe',
    'acces':r'C:\Program Files\Microsoft Office\root\Office16\MSACCESS.EXE',
    'adobe':r'C:\Program Files\Adobe\Acrobat DC\Acrobat\Acrobat.exe',
    # 'teclado':r'C:\Windows\system32\osk.exe', La app del teclado por el momento arroja un error..
    'launcher':r'C:\Users\LENOVO\AppData\Local\Programs\Ankama Launcher\Ankama Launcher.exe',
    'netbeans':r'C:\Program Files\NetBeans 8.2\bin\netbeans64.exe',
    # 'obs': r'C:\Program Files\obs-studio\bin\bit\obs64.exe' error al abrir la app devido a permisos internos...
    'virtual': r'C:\Program Files\Oracle\VirtualBox\VirtualBox.exe'

}

  
def Take_query(): # metodo principal para comandos...
  
    Hello() 
      
    bucle = True
    while(bucle == True): 
          
        query = takeCommand().lower() 
        if "abrir youtube" in query: 
            speak("abriendo youtube") 
              
            webbrowser.open("www.youtube.com") 
            continue

        if "video"in query: 
            
            speak("Abriendo video en youtube") 
            
            webbrowser.open("https://www.youtube.com/results?search_query=" + str(query))
            continue

        if "Google"in query: 
            
            speak("Abriendo video en youtube") 
            
            webbrowser.open("https://www.google.com") 
            continue

        if "abrir código" in query: 
            speak("abriendo codigo de mi creador") 
              
            webbrowser.open("https://github.com/Camilocsr/Daniela.git") 
            continue
              
        elif "día"in query: 
            tellDay() 
            continue

        elif "comandos" in query:
            speak('Abrindo lista de comandos...')
            interfas()
            continue
          
        elif "dime la hora" in query: 
            tellTime() 
            continue
          
        
        elif "adiós" in query: 
            
            speak("Feliz dia, gracias por usarme y espera mis proximas actualizaciones...")
            exit()
          
        elif "en wikipedia" in query: 
              
            speak("Buscando por ti en wikipedia... ")  

            try:
                query = query.replace("wikipedia", "") 
                result = wikipedia.summary(query, sentences=4) 
                speak("Tu busqueda en wikipedia es") 
                speak(result)
            except:
                speak('Tu busqueda no coinside con ninguna pagina en wikipedia.')
          
        elif "dime tu nombre" in query:
            speak("Yo me llamo daniela...")  

        elif "creador"in query: 
            speak("Fuy creada por el programador y desarrolador de sofware, camilo solano rodriguez, el 1 de diciembre del 2022 a las 8:22pm, a peticion de su profesor de universidad, jhon jhairo mazo perez.") 
        
        elif 'abrir' in query:
            for programs in apps:
                if programs in query:
                    speak('Abriendo la aplicacion solicitada')
                    os.startfile(apps[programs])

if __name__ == '__main__': # metodo principal de todo el programa...
    Take_query()