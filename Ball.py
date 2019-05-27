import random

class Ball():

    def __init__(self, canvas):
        self.canvas = canvas
        self.circle = None

        self.xStart = 0
        self.yStart = 0
        self.farbe = "red"
        self.durchmesser = 10

        # für die Animation:
        self.moveX = 0
        self.moveX = 0
        self.newCounter = 100
        self.counter = 100
        self.wait = 50
        self.isMoving = False


    def setStartPosition(self, x, y):
        self.xStart = x
        self.yStart = y

    def display(self):
        coord = [self.xStart, self.yStart, self.xStart + self.durchmesser, self.yStart + self.durchmesser]
        self.circle = self.canvas.create_oval(coord, fill=self.farbe)

    def moveRelative(self, diffX, diffY):

        if not self.isMoving:       # nur ausführen, wenn aktuell keine Animation läuft
            self.isMoving = True            # setzen den Indikator, dass die Animation gerade läuft
            self.moveX = diffX
            self.moveY = diffY
            self.counter = self.newCounter    # setze Anzahl der Durchgänge, um den Zielpunkt zu erreichen
            self.__move()

    def moveToPosition(self, newX, newY, loops):

        if not self.isMoving:
            self.isMoving = True

            # ermittle die aktuelle x- und y-Koordinate des Balls
            coordinates = self.canvas.coords(self.circle)
            x = coordinates[0]
            y = coordinates[1]

            # abhängig von der gewählten Geschwindigkeit wird die Anzahl der Durchläufe und die X- und Y-Änderung nach jedem Durchgang berechnet
            self.counter = loops
            self.moveX = int((newX - x) / loops)
            self.moveY = int((newY - y) / loops)
            self.__move()           # starte die Animation

    # diese Methode wird solange selbst aufgerufen, bis die Animation beendet ist
    def __move(self):

        self.canvas.move(self.circle, self.moveX, self.moveY)
        self.canvas.update()

        # falls noch nicht alle Durchläufe absolviert wurden, soll die Methode erneut ausgeführt werden.
        if self.counter > 1:
            self.counter = self.counter -1
            self.canvas.after(self.wait, self.__move)   # wichtig, damit andere Elemente der GUI während der Animation auch noch angesprochen werden können!!!
        else:
            self.isMoving = False
            self.canvas.after(self.wait, self.moveNext) # die Methode moveNext() kann überschrieben werden und wird aufgerufen, wenn die bisherige Animation beendet wurde

    def moveNext(self):
        pass

