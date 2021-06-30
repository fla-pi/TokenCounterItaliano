import os
import ssl
import PySimpleGUI as sg
import nltk
from nltk.probability import FreqDist

sg.theme('DarkBlue3')   

layout = [  [sg.Text('')],
            [sg.Text('''SOLO la prima volta che usi questo programma, scarica da qui i contenuti di 'book': '''), sg.Button('Installa NLTK data')],
            [sg.Text('')],
            [sg.Text('File/cartella'), sg.Input(size=(75,1),key=1)],
            [sg.Text('IMPORTANTE: Assicurati che il file sia codificato in utf-8!'), sg.Button('Apri file...'), sg.Button ('Apri cartella...')],
            [sg.Text('')],
            [sg.Text('''
Il numero dei token del tuo testo (per i file):
'''), sg.Input(key=2)],
            [sg.Text('''
Da qui puoi controllare la tokenizzazione per i file (mostra un campione del testo)
OPPURE il numero di token per file nella cartella:''')],
            [sg.Output(size=(75,15), key="-OUTPUT-")],
            
            [sg.Button("Conta i token"), sg.Button("Esci"), sg.Text('                                                                                    https://github.com/fla-pi')]]


window = sg.Window('Token Counter for Italian', layout)


while True:
    event, values = window.read()
                
    if event in (None, 'Esci'): 
        break
    elif event in (None, 'Apri file...'):
        def browse():
            window[2].update('') 
            path = sg.popup_get_file(message = None,
            title='Browse file',
            default_path="",
            default_extension="",
            save_as=False,
            multiple_files=False,
            file_types=(("Text Files", ".txt .TXT"),("All Files", ".")),
            no_window=True,
            size=(50, 50),
            button_color=('Black','LightGrey'),
            background_color=('LightGrey'),
            text_color=('Black'),
            icon=None,
            font=None,
            no_titlebar=False,
            grab_anywhere=True,
            keep_on_top=False,
            location=(None, None),
            initial_folder=None)
            window[1].update(path)
            window['-OUTPUT-'].update('')
            
        browse()
    elif event in (None, 'Apri cartella...'):
        def browse_dir():
            window[2].update('')  
            path = sg.popup_get_folder(message = None,
            title ='Browse directory',
            default_path = "",
            no_window=True,
            size=(50, 50),
            button_color=('Black','LightGrey'),
            background_color=('LightGrey'),
            text_color=('Black'),
            icon=None,
            font=None,
            no_titlebar=False,
            grab_anywhere=True,
            keep_on_top=False,
            location=(None, None),
            initial_folder=None)
            window[1].update(path)
            window['-OUTPUT-'].update('')
        browse_dir()
    elif event in (None, 'Installa NLTK data'):
        try:
            _create_unverified_https_context = ssl._create_unverified_context
        except AttributeError:
            pass
        
        else:
            ssl._create_default_https_context = _create_unverified_https_context

        nltk.download()
    elif event in (None, 'Conta i token'):
        def main():
            path = values[1]
            window['-OUTPUT-'].update('')
            if os.path.isfile(path):
                if len(path)>0:
                    try:
                        raw_txt = open(path, encoding = 'utf-8').read()
                        tokenized = nltk.word_tokenize(raw_txt, language = 'italian')
                        fdist = FreqDist(tokenized)
                        num = int(fdist.N())
                        window[2].update(num)
                        p = int((len(tokenized)*15)/100)
                        if num <= 1000:
                            print(tokenized[:p])
                        else:
                            print(tokenized[:150])
                    except UnicodeDecodeError:
                        print('Errore. Assicurati che il tuo file sia in utf-8!')
                    except:
                        print('Qualcosa è andato storto')
            elif os.path.isdir(path):
                dir_name = os.path.basename(path)
                tok_sum = 0
                print('Token nei file nella cartella ' + dir_name + '''
''')
                if len(path)>0:
                    try:
                        for file in os.listdir(path):
                            if file.endswith(".txt"):    
                                raw_txt = open(path+'/'+file, encoding = 'utf-8').read()
                                tokenized = nltk.word_tokenize(raw_txt, language = 'italian')
                                fdist = FreqDist(tokenized)
                                num = int(fdist.N())                
                                tok_sum += num
                                print(file+ " contiene ", num, "token")
                        print ('''
Il numero di token nella cartella '''+ dir_name+ " è", tok_sum)
                        tok_sum = 0
                    except UnicodeDecodeError:
                        print('Errore! Assicurati che i tuoi file siano in utf-8')
                    except:
                        print('Qualcosa è andato storto. Assicurati di aver scaricato "book" da NLTK data')
          
        main()
    
            

                
                    
window.Close()
