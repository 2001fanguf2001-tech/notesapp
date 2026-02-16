from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

class NotesApp(App):
    def build(self):
        layout = BoxLayout(orientation="vertical")

        self.input = TextInput(hint_text="Введите заметку")
        layout.add_widget(self.input)

        btn = Button(text="Сохранить")
        btn.bind(on_press=self.save_note)
        layout.add_widget(btn)

        self.label = Label(text="")
        layout.add_widget(self.label)

        return layout

    def save_note(self, instance):
        text = self.input.text
        if text:
            self.label.text = "Сохранено!"
            self.input.text = ""

if __name__ == "__main__":
    NotesApp().run()
