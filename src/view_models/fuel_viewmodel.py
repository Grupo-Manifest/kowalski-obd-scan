from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivy.lang import Builder

from scanner_connection.obd_query_handler import OBDQueryHandler

Builder.load_file("views/fuel_view.kv")
class FuelView(Screen):
    current_fuel_level    = StringProperty()
    current_fuel_pressure = StringProperty()

    def __init__(self, **kwargs):
        super(FuelView, self).__init__(**kwargs)
        obd_query = OBDQueryHandler()

        self.current_fuel_level    = str(obd_query.get_fuel_level())
        self.current_fuel_pressure = str(obd_query.get_fuel_pressure())
