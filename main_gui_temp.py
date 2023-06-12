import sys, os
import logging
import qdarkstyle
from PyQt5 import uic
from pathlib import Path
from PyQt5.QtWidgets import QMainWindow,QApplication
from ..core.gui_funcs import main_gui_funcs as gui
from ..util.log_util.log_util_funcs import load_config

class MyMainWindow(QMainWindow):
    def __init__(self, parent = None):
        super(MyMainWindow, self).__init__(parent)

    def init_gui(self, ui = None):
        logging.getLogger('').info('Start init gui widgets!')
        if ui == None:
            ui = str(Path(__file__).parent.parent/ "res" / "ui" / "main_gui.ui")
        if os.path.exists(ui):
            self.ui = ui
            try:
                uic.loadUi(ui, self)
                logging.getLogger('').info('Succeed in loading main gui ui file.')
            except Exception as e:
                logging.getLogger('').exception('Failed to load main gui ui file.')
                return
        else:
            logging.getLogger('').exception('OOPS, ui file {} is not existing.'.format(ui))
            return
        gui.set_button_icons(self)
        gui.signal_slot_connection(self)

def main():
    load_config()
    QApplication.setStyle("windows")
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    myWin = MyMainWindow()
    myWin.init_gui()
    myWin.setWindowTitle()
    myWin.show()
    sys.exit(app.exec_())    

if __name__ == "__main__":
    main()