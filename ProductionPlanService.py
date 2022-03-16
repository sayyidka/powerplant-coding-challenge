from PowerplantGenerator import PowerplantGenerator
from MeritOrderer import MeritOrderer


class ProductionPlanService:
    """Give the production plan based on the load, fuels and powerplants input"""

    def __init__(self, payload):
        self.load = payload["load"]
        self.fuels = payload["fuels"]
        self.powerplants_input = payload["powerplants"]
        self.powerplant_objects = []
        self.generator = PowerplantGenerator(self.fuels)

        self._instanciate_powerplants()
        self.merit_orderer = MeritOrderer(
            self.load, self.fuels, self.powerplant_objects
        )

    def _instanciate_powerplants(self):
        """Create powerplant objects"""
        for pp in self.powerplants_input:
            powerplant = self.generator.create_instance(pp)
            self.powerplant_objects.append(powerplant)

    def give_production_plan(self):
        """Calculate how much each powerplant need to produce

        Returns:
            list: list of powerplant dicts with name and load
        """
        return self.merit_orderer.order_powerplants()
