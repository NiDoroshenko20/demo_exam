from PySide6 import QtWidgets, QtCore, QtGui
from src.client.api.session import Session
from server import start_server
import multiprocessing



class MainWindow(QtWidgets.QMainWindow):
    session: Session = Session()

    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        multiprocessing.Process(target=self.start_server)
        self.__init_ui()
        self.__setting_ui()
    
    def __init_ui(self) -> None:
        self.central_widget = QtWidgets.QWidget()
        self.user_profile = None # TODO
        self.authorization_menu = None # TODO
    
    def start_server(self) -> multiprocessing.Process:
        self.server_process = multiprocessing.Process(target=start_server)
        self.server_process.start()
        while not self.session.server_available:
            self.session.check_connect()
    
    def __setting_ui(self) -> None:
        self.setCentralWidget(self.central_widget)