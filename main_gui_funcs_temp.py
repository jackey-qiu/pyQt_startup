import logging
import os
from pathlib import Path
from PyQt5 import QtGui
from PyQt5.QtCore import QSize

def signal_slot_connection(self):
    raise NotImplementedError

def set_button_icons(self):
    root = Path(__file__).parent.parent.parent/ "res" / "icons"
    #self.setWindowIcon(QtGui.QIcon(str(root/ "calculator.png")))
    raise NotImplementedError
