from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from view_models.main_viewmodel import MainView

class ObdMain(App):
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(MainView())

        return screen_manager


if __name__ == "__main__":
    ObdMain().run()
