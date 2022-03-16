from Gasfired import Gasfired
from Turbojet import Turbojet
from Windturbine import Windturbine


class PowerplantGenerator:
    """Create powerplant objects based on the given subclass"""

    def __init__(self, fuels):
        self.fuels = fuels

    def create_instance(self, specs):
        """Create powerplant object

        Args:
            specs (dict): the powerplant's characteristics

        Returns:
            Powerplant: the powerplant's sub-class based object
        """
        if specs["type"] == "gasfired":
            return Gasfired(specs, self.fuels["gas(euro/MWh)"])
        elif specs["type"] == "turbojet":
            return Turbojet(specs, self.fuels["kerosine(euro/MWh)"])
        elif specs["type"] == "windturbine":
            return Windturbine(specs, self.fuels["wind(%)"])
