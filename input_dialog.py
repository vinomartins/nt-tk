from textual.screen import ModalScreen
from textual.widgets import Input, Button, Static
from textual.containers import Vertical, Horizontal


class TwoIntInputDialog(ModalScreen[tuple[int, int]]):
    """Dialog to input two integers."""

    def __init__(self, title: str, a_label="a", b_label="b"):
        super().__init__()
        self.title = title
        self.a_label = a_label
        self.b_label = b_label

    def compose(self):
        yield Vertical(
            Static(self.title, classes="title"),
            Input(placeholder=self.a_label, id="a"),
            Input(placeholder=self.b_label, id="b"),
            Horizontal(
                Button("OK", id="ok", variant="primary"),
                Button("Cancelar", id="cancel"),
            ),
            id="dialog",
        )

    def on_button_pressed(self, event: Button.Pressed):
        if event.button.id == "ok":
            try:
                a = int(self.query_one("#a", Input).value)
                b = int(self.query_one("#b", Input).value)
                self.dismiss((a, b))
            except ValueError:
                self.notify("Por favor, insira valores inteiros para a e b")
        else:
            self.dismiss(None)

class OneIntInputDialog(ModalScreen[int]):
    """Dialog to input one integer."""

    def __init__(self, title: str, n_label="n"):
        super().__init__()
        self.title = title
        self.n_label = n_label

    def compose(self):
        yield Vertical(
            Static(self.title, classes="title"),
            Input(placeholder=self.n_label, id="n"),
            Horizontal(
                Button("OK", id="ok", variant="primary"),
                Button("Cancelar", id="cancel"),
            ),
            id="dialog",
        )

    def on_button_pressed(self, event: Button.Pressed):
        if event.button.id == "ok":
            try:
                n = int(self.query_one("#n", Input).value)
                self.dismiss(n)
            except ValueError:
                self.notify("Por favor, insira um valor inteiro para n")
        else:
            self.dismiss(None)

