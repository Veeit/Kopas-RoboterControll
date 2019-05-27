from tkinter import *
import requests

# Diese Datei muss separat gestartet werden.

class Client():

    # Die Ein- und Ausgabefelder
    inputRow = None
    inputColumn = None
    output = None

    def __init__(self):
        self.__root = Tk()
        self.__root.title("Roboter - Client")
        self.__canvas = Canvas(self.__root, width=400, height=400)

        self.__drawContent()

    def display(self):
        self.__root.mainloop()

    # Zeichne die GUI
    def __drawContent(self):
        Label(self.__root, text="Zeile (relativ)").grid(row=0)
        Label(self.__root, text="Spalte  (relativ)").grid(row=1)

        Client.inputRow = Entry(self.__root)
        Client.inputColumn = Entry(self.__root)

        Client.inputRow.grid(row=0, column=1)
        Client.inputColumn.grid(row=1, column=1)

        buttonRelative = Button(self.__root, text="absenden (relativ)", command=self.sendRelative)
        buttonRelative.grid(sticky="W", row=3, column=0)

        buttonRelative = Button(self.__root, text="start", command=self.sendReset)
        buttonRelative.grid(sticky="W", row=4, column=0)

        label = Label(self.__root, text="Rückmeldung:", anchor="w").grid(sticky="W", row=5, column = 0)
        Client.output = Label(self.__root, text="")
        Client.output.grid(sticky="W", row=5, column=1)

    # Sende die neue Roboterposition (relativ)
    @classmethod
    def sendRelative(event):
        Client.output.configure(text='')        # Meldung löschen

        try:
            row = Client.inputRow.get()
            column = Client.inputColumn.get()
            payload = {'xSteps': row, 'ySteps': column}
            req = requests.post('http://localhost:4996/move', params=payload)
            Client.output.configure(text=req.text)
        except:
            Client.output.configure(text='Server nicht erreichbar!')


    # Setze die Roboterposition zurück
    @classmethod
    def sendReset(event):
        Client.output.configure(text='')        # Meldung löschen

        try:
            req = requests.post('http://localhost:4996/start')
            Client.output.configure(text=req.text)
        except:
            Client.output.configure(text='Server nicht erreichbar!')



# Erzeuge die GUI und stelle sie dar
client = Client()
client.display()