import math

from Powerplant import Powerplant


class Windturbine(Powerplant):
    """Wind turbine powerplant

    Args:
        Powerplant (Powerplant): abstract parent class
    """

    def __init__(self, specs, fuel):
        super().__init__(specs, fuel)

    def attribute_production(self, given_load):
        """Set production for the wind turbine, to be included
        in the response object

        Args:
            given_load (int): the attributed load

        Returns:
            dict: the powerplant object with its attributed production
        """

        return {"name": self.name, "p": given_load}

    def compute_wind_production(self, load):
        """Give the production to attribute to this powerplant, based on its pmax and
        its efficiency

        Args:
            load (int): the remaining load from the input

        Returns:
            int: the cost per 1 MWh
        """

        production = self.pmax * (self.mwh_price / 100)
        wind_production = int(math.ceil(production))
        if wind_production >= load:
            return load
        return wind_production

    def compute_cost_per_mwh(self):
        pass
