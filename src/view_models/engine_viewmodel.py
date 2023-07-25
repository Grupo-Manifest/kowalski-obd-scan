from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivy.lang import Builder

from scanner_connection.obd_query_handler import OBDQueryHandler

Builder.load_file("views/engine_view.kv")
class EngineView(Screen):
    current_engine_rpm     = StringProperty()
    current_engine_coolant = StringProperty()
    current_engine_load    = StringProperty()
    
    def __init__(self, **kwargs):
        super(EngineView, self).__init__(**kwargs)
        obd_query = OBDQueryHandler()

        self.current_engine_rpm     = str(obd_query.get_engine_rpm())
        self.current_engine_coolant = str(obd_query.get_coolant_temperature())
        self.current_engine_load    = str(obd_query.get_engine_load())
