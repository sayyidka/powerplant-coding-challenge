from Powerplant import Powerplant


class Turbojet(Powerplant):
    """Turbojet powerplant

    Args:
        Powerplant (Powerplant): abstract parent class
    """

    def __init__(self, specs, fuel):
        super().__init__(specs, fuel)

    def attribute_production(self, given_load):
        """Set production for the turbojet, to be included
        in the response object

        Args:
            given_load (int): the attributed load

        Returns:
            dict: the powerplant object with its attributed production
        """
        return {"name": self.name, "p": given_load}

    def compute_cost_per_mwh(self, load):
        """Give cost per MWh based on the price of gas per MWh
        baased on the pmax and the efficiency

        Args:
            load (int): the remaining load from the input

        Returns:
            int: the cost per 1 MWh
        """
        return (self.mwh_price * load / self.efficiency) / load
