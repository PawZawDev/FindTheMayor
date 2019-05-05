"""
Written by Pawel Zawierucha
Using BeautifulSoup to scrape data from wikipedia
Using PyQt5 for GUI

This is the GUI part
"""
#gui libraries
import sys
from PyQt5 import QtGui,QtWidgets,QtCore
#from PyQt5 import 

#logic libraries
from FindTheMayorOnClass import FindTheMayor

class Window(QtWidgets.QMainWindow):

    def __init__(self):
        self.myx=10
        self.myy=25
        self.mydistance=130
        self.mysize=(100,35)

        super().__init__()
        self.setGeometry(200,200,self.mydistance*2,self.myy*4)
        self.setWindowTitle("FindTheMayor")
        #self.setWindowIcon(QtGui.QIcon("feed.png"))

        self.box_init()
        self.button_init()
        self.action_init()
        self.show()

    def click_find(self):
        city=self.input_box.text()
        answer=FindTheMayor.gui_do_magic(city)
        self.answer_box.setText(answer)

    def close_app(self):
        # print("App closed with escape")
        sys.exit()

    def box_init(self):
        self.input_box=QtWidgets.QLineEdit(self)
        self.input_box.resize(self.mysize[0],self.mysize[1]-12)
        self.input_box.move(self.myx,self.myy)
        self.input_box.setText("Enter your city")
        self.input_box.setAlignment(QtCore.Qt.AlignCenter)

        self.answer_box=QtWidgets.QTextBrowser(self)
        self.answer_box.resize(self.mysize[0],self.mysize[1])
        self.answer_box.move(self.myx+self.mydistance,self.myy)
        self.answer_box.setText("Your mayor")
        #self.answer_box.setAlignment(QtCore.Qt.AlignCenter)
        self.answer_box.setAlignment(QtCore.Qt.AlignCenter)
    
    def button_init(self):
        self.button=QtWidgets.QPushButton("Find The Mayor",self)
        self.button.move(self.mydistance/2+self.myx,self.myy*2.5)
        self.button.clicked.connect(self.click_find)

    def action_init(self):
        self.do_it=QtWidgets.QAction("Find The Mayor",self)
        self.do_it.setShortcut("Return")
        self.do_it.triggered.connect(self.click_find)        
        self.exitAction=QtWidgets.QAction("Quit",self)
        self.exitAction.setShortcut("Esc")
        self.exitAction.triggered.connect(self.close_app)

        self.mainMenu=self.menuBar()
        self.mainMenu.addAction(self.exitAction)
        self.mainMenu.addAction(self.do_it)

def main():    
    app=QtWidgets.QApplication(sys.argv)
    my_gui=Window()
    sys.exit(app.exec_())
main()
