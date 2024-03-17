from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

import random

class ScatterTextWidget(BoxLayout):
    def change_label_colour(self, *args):
        colour = [random.random() for i in range(3)] + [1]
        label = self.ids['my_label']  # refers to the label id defined in he kv file
        label.color = colour


class TutorialApp(App):
    def build(self):
        return ScatterTextWidget()


if __name__ == "__main__":
    TutorialApp().run()
