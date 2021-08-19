# TokenCounterItaliano
Programma in Python con GUI per contare i token di un file text o di tutti quelli in una directory.

Sono disponibili anche le applicazioni per Windows, MacOS e Linux, utilizzabili senza installare le dipendenze e senza l'utilizzo di Python. 

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
**In alternativa:**
**- Versione .exe per Windows x64**
https://sourceforge.net/projects/tokencounterita/files/win_TokenCounterItaliano%28x64%29.rar per il download.

**- Versione .app per macOS x64**
https://sourceforge.net/projects/tokencounterita/files/TokenCounterItaliano%28macOSx64%29.rar/download

Per queste versioni **non è necessario installare le dipendenze**

## Utilizzo
Lanciare il programma. Se si utilizza per la prima volta il programma e non si è mai scaricato nltk-data, premere su _Installa NLTK DATA_.

Selezionare il file .txt (o la cartella contenente file .txt) e contare i token. Se si apre un file, verrà mostrata una parte di testo, 
altrimenti il totale per file e per cartella di token.

![alt text](https://github.com/fla-pi/TokenCounterItaliano/blob/main/demo.gif)
