from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.lang import Builder

from .fuel_viewmodel import FuelView
from .engine_viewmodel import EngineView
from .status_viewmodel import StatusView
from .diagnostics_viewmodel import DiagnosticsView

Builder.load_file("views/main_view.kv")
class MainView(Screen):
    def __init__(self, **kwargs):
        super(MainView, self).__init__(**kwargs)

        self.fuel_viewmodel = FuelView()
        self.engine_viewmodel = EngineView()
        self.status_viewmodel = StatusView()
        self.diagnostics_viewmodel = DiagnosticsView()
