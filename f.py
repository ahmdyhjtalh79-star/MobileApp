import os
# این خط به Kivy می‌گه از DirectX (Angle) استفاده کنه، نه OpenGL
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

# تنظیمات ظاهری (تم دارک)
Window.clearcolor = (0.1, 0.1, 0.1, 1) 

class MyMobileApp(App):
    def build(self):
        self.title = "My First Mobile App"
        
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        title_label = Label(
            text="Hello Mobile! 📱",
            font_size='40sp',
            color=(1, 1, 1, 1),
            size_hint_y=0.2
        )
        layout.add_widget(title_label)
        
        self.text_input = TextInput(
            hint_text="Type something here...",
            font_size='20sp',
            size_hint_y=0.2,
            multiline=False
        )
        layout.add_widget(self.text_input)
        
        btn = Button(
            text="Click Me!",
            font_size='24sp',
            size_hint_y=0.2,
            background_color=(0.2, 0.6, 1, 1)
        )
        btn.bind(on_press=self.on_button_click)
        layout.add_widget(btn)
        
        self.result_label = Label(
            text="",
            font_size='24sp',
            color=(0.2, 0.8, 0.2, 1),
            size_hint_y=0.2
        )
        layout.add_widget(self.result_label)
        
        return layout

    def on_button_click(self, instance):
        user_text = self.text_input.text
        if user_text:
            self.result_label.text = f"You typed: {user_text}"
        else:
            self.result_label.text = "Please type something!"

if __name__ == '__main__':
    MyMobileApp().run()