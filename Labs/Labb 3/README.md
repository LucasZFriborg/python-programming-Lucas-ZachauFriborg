# Laboration 3 - Linjär klassificering

## Beskrivning
Detta program läser in en csv-fil med oklassificerade punkter, delar upp dem i två klasser (**1** och **0**) med hjälp av en rak linje och visar resultatet i ett spridningsdiagram. 
Programmet använder en **linjär funktion** på formen `y = kx + m` för att skilja datapunkterna åt. 
Om en punkt ligger **ovanför** linjen klassas den som **Class 1**. 
Om punkten ligger **under** linjen klassas den som **Class 0**.

## Innehåll

### Data
Mapp som innehåller filerna med den oklassificerade datan (`unlabelled_data.csv`) och den klassificerade datan (`labelled_data.csv`).

### Labb3_Programmering.pdf
Instruktionsfil för laborationen.

### Labb3.py
Pythonfil som läser in datan, klassificerar punkterna och visualiserar resultatet.

## Krav på installation
- **Python3**
- **Numpy**
- **Matplotlib**
- **Pandas**

## Användning
1. Klona eller ladda ner projektmappen.
2. Se till att alla filer ligger i mappen som programfilen körs ifrån.
3. Kör filen `labb3.py` för att se klassificeringen av punkterna i ett diagram
4. Öppna filen `labelled_data.csv` för att se klassificeringen i en tabell