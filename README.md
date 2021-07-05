# TokenCounterItaliano
Programma in Python con GUI per contare i token di un file text o di tutti quelli in una directory.

## Istruzioni per l'installazione
Per utilizzare lo **script Python**, installare le dipendenze:
```
PySimpleGUI
nltk
```
può essere fatto installandole direttamente da requirements.txt:

```
python pip install -r requirements.txt
```

E' disponibile anche la **versione .exe per Windows x64** (a breve saranno disponibili anche le applicazioni per Linux e Mac):
https://sourceforge.net/projects/tokencounterita/files/win_TokenCounterItaliano%28x64%29.rar per il download.
Per la versione .exe **non è necessario installare** le dipendenze.

## Utilizzo
Lanciare il programma. Se si utilizza per la prima volta il programma e non si è mai scaricato nltk-data, premere su _Installa NLTK DATA_.
Selezionare il file .txt (o la cartella contenente file .txt) e contare i token. Se si apre un file, verrà mostrata una parte di testo, 
altrimenti il totale per file e per cartella di token.

![alt text](https://github.com/fla-pi/TokenCounterItaliano/blob/main/demo.gif)
