# Importación de Rich
from rich.console import Console

# Creación de instancia de objeto
terminal = Console()

# Test de funcionamiento de librería
# terminal.print("[bold green]Hola Verde[/]")
# terminal.print("[italic yellow]Hola Amarillo[/]")
# terminal.print(":smiley:")

# Logotipo Skell's ADO
logo = """
  ╔═════════════════════════╗
[purple]┌─[/ purple]║ ▄▄▄ █  ▄ ▄▄▄ ▄  ▄ █ ▄▄▄ ║
[purple]│ [/ purple]║ █▄▄ █▄▀  █▄▄ █  █   █▄▄ ║
[purple]│ [/ purple]║ ▄▄█ █ ▀▄ █▄▄ █▄ █▄  ▄▄█ ║
[purple]│ [/ purple]║ [bold cyan]─────  A   D   O  ─────[/ bold cyan] ║
[purple]│ [/ purple]╚═════════════════════════╝
[purple]└─────────────────────────┘[/ purple]
"""

terminal.print(logo)
