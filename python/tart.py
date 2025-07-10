# Importación de Rich
from rich.console import Console

# Creación de instancia de objeto
terminal = Console()

# Test de funcionamiento de librería
# terminal.print("[bold green]Hola Verde[/]")
# terminal.print("[italic yellow]Hola Amarillo[/]")
# terminal.print(":smiley:")

# Logotipo Skell's ADO
def logo():
  return """
    ╔═════════════════════════╗   ╔══════════════════════════════════════════════╗
  [purple]┌─[/ purple]║ ▄▄▄ █  ▄ ▄▄▄ ▄  ▄ █ ▄▄▄ ║ [purple]┌─[/ purple]║ Skell's ADO es un software basado en hosting ║
  [purple]│ [/ purple]║ █▄▄ █▄▀  █▄▄ █  █   █▄▄ ║ [purple]│ [/ purple]║ que permite gestionar clientes, ventas, in-  ║
  [purple]│ [/ purple]║ ▄▄█ █ ▀▄ █▄▄ █▄ █▄  ▄▄█ ║ [purple]│ [/ purple]║ ventario y más dentro de una empresa.        ║
  [purple]│ [/ purple]║ [bold cyan]─────  A   D   O  ─────[/ bold cyan] ║ [purple]│ [/ purple]║ [bold cyan] — Todos los créditos a Robert Rodríguez — [/bold cyan]  ║
  [purple]│ [/ purple]╚═════════════════════════╝ [purple]│ [/ purple]╚══════════════════════════════════════════════╝
  [purple]└─────────────────────────┘[/ purple]   [purple]└──────────────────────────────────────────────┘[/ purple]
  """

terminal.print(logo())
