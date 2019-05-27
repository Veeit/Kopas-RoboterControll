from flask import Flask
from flask import request
from Ball import Ball
import json
import threading
from tkinter import *

class feldGui():
    reference = None

    @staticmethod
    def getReference():
        if feldGui.reference == None:
            print("no reference")
        return feldGui.reference

    def __init__(self,root, x, y):
        self.x = x
        self.y = y
        self.root = root
        feldGui.reference = self

    def addCanvas(self):
        self.canvas = Canvas(self.root, width=300, height=300)
        self.canvas.pack()

    def createPlayGround(self):
        countedY = 0
        countedX = 0
        posX = 0
        posY = 0
        while countedX < self.x:
            posX = posX + 50
            self.canvas.create_line(posX, 0, posX, self.y * 50, fill="#476042", width=1)
            countedX = countedX + 1
        while countedY < self.y:
            posY = posY + 50
            self.canvas.create_line(0, posY, self.x * 50, posY, fill="#476042", width=1)
            countedY = countedY + 1

class feld(feldGui):
    def __init__(self,root,x, y):
        feldGui.__init__(self, root, x,y)
        self.posX = 150
        self.posY = 100

    def addRobi(self):
        self.roboter = Ball(self.canvas)

        self.roboter.farbe = "red"
        self.roboter.durchmesser = 20
        self.roboter.setStartPosition(self.posX + 15, self.posY + 15)
        self.roboter.display()

        return self.roboter

    def move(self, vertical, hoizontal):
        vertical = vertical / 2
        hoizontal = hoizontal / 2
        if (self.posX / 50 + hoizontal < self.x - 1) and (self.posY / 50 + vertical < self.y - 1) and (self.posY / 50 + vertical > 0) and (self.posX / 50 + hoizontal > 0):
            self.roboter.moveRelative(hoizontal, vertical)
            self.posX = hoizontal
            self.posY = vertical

class api(threading.Thread):
    app = Flask(__name__)

    def __init__(self):
        super().__init__()

    def start(self):
        super().start()

    def run(self):
        self.app.run(host='0.0.0.0', port=4996)

    @app.route('/start', methods=['POST'])
    def startNew():
        x = "ok"
        game = feld.getReference()
        game.addCanvas()
        game.addRobi()
        game.createPlayGround()

        y = json.dumps(x)
        return y
    @app.route('/move', methods=['POST'])
    def moveTo():
        move_X = request.args.get('xSteps')
        move_Y = request.args.get('ySteps')
        move_X = int(move_X)
        move_Y = int(move_Y)
        x = "ok"
        y = json.dumps(x)
        game = feld.getReference()
        game.move(move_Y, move_X)
        return y

def startGUI():
    root = Tk()  # Initialisierung des GUI-Frameworks TKinter
    feld(root, 5, 6)
    root.mainloop()

api = api()
api.start()

startGUI()