from .commands import cli
__all__ = ['cli']

# When someone writes from stack.cli import *, they'll only get the cli function
# It's a way to keep your package's interface clean and explicit
# Without __all__, import * would import everything in the module