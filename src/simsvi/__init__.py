# read version from installed package
from importlib.metadata import version
from .simsvi import SVISimulation
from .run_simulation import run_multiple_simulations
__version__ = version("simsvi")