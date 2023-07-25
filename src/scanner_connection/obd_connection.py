import obd
import atexit
from singleton.singleton import Singleton

class OBDConnection(metaclass=Singleton):
    """Singleton class for managing the OBD connection"""

    def __init__(self):
        """Initialize the OBD connection"""
        self.connection = obd.OBD()

        atexit.register(self.close_connection)


    def close_connection(self):
        """Close the OBD connection"""
        if self.connection.is_connected():
            self.connection.close()
