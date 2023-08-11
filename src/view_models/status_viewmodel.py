from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivy.lang import Builder

from scanner_connection.obd_query_handler import OBDQueryHandler

Builder.load_file("views/status_view.kv")
class StatusView(Screen):
    current_speed = StringProperty()

    def __init__(self, **kwargs):
        super(StatusView, self).__init__(**kwargs)
        obd_query = OBDQueryHandler()

        self.current_speed = str(obd_query.get_speed())
