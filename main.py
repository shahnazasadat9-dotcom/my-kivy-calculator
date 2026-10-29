from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class CalculatorApp(App):
    def build(self):
        self.title = "My Calculator"

        root = BoxLayout(
            orientation="vertical",
            padding=10,
            spacing=8
        )

        self.display = TextInput(
            text="",
            font_size=32,
            readonly=True,
            halign="right",
            multiline=False,
            size_hint_y=0.25
        )
        root.add_widget(self.display)

        grid = GridLayout(
            cols=4,
            spacing=6
        )

        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "C", "0", "=", "+"
        ]

        for value in buttons:
            button = Button(
                text=value,
                font_size=26
            )
            button.bind(on_press=self.press)
            grid.add_widget(button)

        root.add_widget(grid)
        return root

    def press(self, button):
        value = button.text

        if value == "C":
            self.display.text = ""

        elif value == "=":
            try:
                expression = self.display.text

                allowed = set("0123456789.+-*/() ")

                if not expression or not all(
                    char in allowed for char in expression
                ):
                    self.display.text = "Error"
                    return

                result = eval(
                    expression,
                    {"__builtins__": {}},
                    {}
                )
                self.display.text = str(result)

            except Exception:
                self.display.text = "Error"

        else:
            if self.display.text == "Error":
                self.display.text = ""

            self.display.text += value


if __name__ == "__main__":
    CalculatorApp().run()