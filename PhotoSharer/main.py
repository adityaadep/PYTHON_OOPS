from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

import wikipedia
import requests
from PIL import Image
from io import BytesIO
import os

Builder.load_file('frontend.kv')


def get_image_file(image_url):
    lst=image_url.split("/")
    return lst[len(lst)-1]

class FirstScreen(Screen):
    def search_image(self):

        # get user query from text input
        query = self.manager.current_screen.ids.user_query.text
        # get wikipedia page and first image link
        print(query)
        page = wikipedia.page(query)

        if not page.images:
            print(f"No images found for the page '{search_string}'.")
            return

        image_url = page.images[0]  # Get the URL of the first image on the page
        print(image_url)
        # download the image
        headers = {'User-Agent': 'Example/1.0 (aditya4855@gmail.com)'}
        try:
            with requests.get(image_url, headers=headers, stream=True) as response:
                response.raise_for_status()

                # Open the image and save it to the specified path
                imagepath = 'files/'+get_image_file(image_url)
                with Image.open(BytesIO(response.content)) as image:
                    image.save(imagepath)
                    print(f"Image downloaded and saved to {imagepath}")
                    self.manager.current_screen.ids.img.source = imagepath

        except requests.exceptions.RequestException as e:
            print(f"Failed to download image. Error: {e}")





class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()
