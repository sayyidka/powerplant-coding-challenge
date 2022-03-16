from abc import ABCMeta, abstractmethod


class Powerplant(object, metaclass=ABCMeta):
    """Abstract powerplant class"""

    @abstractmethod
    def __init__(self, specs, fuel):
        self.name = specs["name"]
        self.type = specs["type"]
        self.efficiency = specs["efficiency"]
        self.pmin = specs["pmin"]
        self.pmax = specs["pmax"]
        self.mwh_price = fuel

    @abstractmethod
    def attribute_production(self):
        pass

    @abstractmethod
    def compute_cost_per_mwh(self):
        pass
