import webbrowser

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.clipboard import Clipboard
import time

from filehsarer import FileSharer

Builder.load_file('frontend.kv')


class CameraScreen(Screen):
    def start(self):
        self.ids.camera.play: True
        self.ids.camera_button.text = 'stop_camera'
        self.ids.camera.texture = self.ids.camera._camera.texture

    def stop(self):
        self.ids.camera.play: False
        self.ids.camera_button.text = 'start_camera'
        self.ids.camera.texture = None

    def capture(self):
        current_time = time.strftime('%Y%m%d-%H%M%S')
        self.filename = current_time +".png"
        self.ids.camera.export_to_png(self.filename)
        self.manager.current = 'image_screen'
        self.manager.current_screen.ids.img.source = self.filename


class ImageScreen(Screen):
    def create_link(self):
        filename = App.get_running_app().root.ids.camera_screen.filename
        fileshare = FileSharer(filename)
        self.url = fileshare.share()
        self.ids.link.text = self.url

    def copy_link(self):
        try:
            Clipboard.copy(self.url)
        except:
            self.ids.link.text= 'create Link first'

    def open_link(self):
        try:
            webbrowser.open(self.url)
        except:
            self.ids.ink.text= 'Create Link first'


class RootWidget(ScreenManager):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


MainApp().run()
