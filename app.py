import logging
logging.basicConfig(filename='info.log',
                    level=logging.INFO,
                    format="%(asctime)s %(levelname)s: %(message)s",
                    )

from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, ListView, ListItem, Static, RichLog
from textual.containers import Horizontal
from textual.reactive import reactive
from input_dialog import TwoIntInputDialog, OneIntInputDialog

from renderer import render

from algorithms.gcd import gcd_with_steps
from algorithms.xgcd import xgcd
from algorithms.primo import primo 
from algorithms.division import division
from algorithms.fermat import fermat

# from algorithms.naive_factor import naive_factorization
# from algorithms.fermat import fermat_factorization
# from algorithms.crt import crt


class OutputPanel(RichLog):
    def __init__(self): 
        super().__init__(markup=True)


class NumberTheoryLab(App):
    CSS = """
    Horizontal {
        height: 100%;
    }

    ListView {
        width: 32%;
        border: solid green;
    }

    OutputPanel {
        width: 68%;
        border: solid blue;
        padding: 1;
        overflow-y: auto;
    }
    """

    BINDINGS = [
        ("q", "quit", "Quit"),
    ]

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        with Horizontal():
            self.menu = ListView(
                ListItem(Static("Divisão euclidiana", name = "div")),
                ListItem(Static("MDC (Alg. de Euclides)", name = "gcd")),
                ListItem(Static("Teste de primalidade", name = "primo")),
                ListItem(Static("Fatoração por Fermat", name = "fermat")),
                ListItem(Static("Inverso módulo m (n. impl)"), name = "inversomod"),
                ListItem(Static("MDC extendido (n. impl)", name = "xgcd")),
                ListItem(Static("Teorema Chinês dos Restos (n. impl)")),
            )
            yield self.menu
            self.output = OutputPanel()
            yield self.output
        yield Footer()

    async def on_list_view_selected(self, event: ListView.Selected):
        list_item = event.item.children[0]
        choice = list_item.name


        if choice == "gcd":
            await self.run_gcd()

        elif choice == "div":
            await self.run_div()

        elif choice == "primo":
            await self.run_primo()

        elif choice == "fermat":
            await self.run_fermat()

        elif choice == "xgcd":
            self.run_xgcd()
        # elif choice == "Naive Factorization":
        #     self.run_naive_factor()
        #
        # elif choice == "Fermat Factorization":
        #     self.run_fermat()
        #
        # elif choice == "Chinese Remainder Theorem":
        #     self.run_crt()


    async def run_gcd(self):
        def on_result(result):
            logging.info(result)
            if result is None:
                return
            a, b = result
            data = gcd_with_steps(a, b)
            self.output.clear()
            self.output.write(render(data))

        await self.push_screen(
            TwoIntInputDialog("Insira os valores de a e b"),
            on_result
        )
        

    async def run_div(self):
        def on_result(result):
            logging.info(result)
            if result is None:
                return
            a, b = result
            data = division(a, b)
            self.output.clear()
            self.output.write(render(data))

        await self.push_screen(
            TwoIntInputDialog("Insira os valores de a e b (positivos)"),
            on_result

        )
    async def run_primo(self):
        logging.info("run_primo: inicio" )
        def on_result(result):
            logging.info("run_primo:", result)
            if result is None:
                return
            p = result
            data = primo(p)
            self.output.clear()
            self.output.write(render(data))

        await self.push_screen(
            OneIntInputDialog("Insira o valor de n"),
            on_result
        )


    async def run_fermat(self):
        logging.info("run_fermat: inicio" )
        def on_result(result):
            logging.info("run_fermat:", result)
            if result is None:
                return
            p = result
            data = fermat(p)
            self.output.clear()
            self.output.write(render(data))

        await self.push_screen(
            OneIntInputDialog("Insira o valor de n"),
            on_result
        )

    # def run_xgcd(self):
    #     result = xgcd(240, 46)
    #     self.output.update(render(result))

    # def run_naive_factor(self):
    #     result = naive_factorization(360)
    #     self.output.update(render(result))
    #
    #
    # def run_crt(self):
    #     congruences = [(2, 3), (3, 5), (2, 7)]
    #     result = crt(congruences)
    #     self.output.update(render(result))
    #

if __name__ == "__main__":
    NumberTheoryLab().run()

