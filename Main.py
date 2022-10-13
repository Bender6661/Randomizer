from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import random
from ui import Ui_Dialog

#Create application
app = QtWidgets.QApplication(sys.argv)

#Create form and init UI
Dialog = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
Dialog.show()
num_list = ["ОРЁЛ", "РЕШКА", "СВАТ"]

#Hook logic
def bp ():
    h = random.choice(num_list)
    resuilt = str(h)
    ui.lineEdit.setText( resuilt )


ui.pushButton.clicked.connect( bp )

#Run main loop
sys.exit(app.exec_())


    
  
    