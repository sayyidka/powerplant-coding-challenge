from Windturbine import Windturbine


class MeritOrderer:
    """Determine the order on which powerplant should be used and how much load it should be given.
    If there is wind, windturbines should be always used at first as it has no pmin and no production cost (at least in this exercise).
    Next, we choose between gas-turbine and turbojet depending on their own cost-per-MWh, including the 100 pmin needed for the gas-turbine.
    Powerplants are selected by the cheapest cost-per-MWh one after the other until the sum of the selected powerplants production equals
    the needed load.
    """

    def __init__(self, load, fuels, powerplants):
        self.load = load
        self.fuels = fuels
        self.powerplants = powerplants
        self.order = []

    def order_powerplants(self):
        """Order powerplants from the cheapest cost per MWh to the most expensive

        Returns:
            list: The selected powerplants as a list of dict
        """
        # If there is wind, windturbines are selected first
        if self.fuels["wind(%)"] > 0:
            for pp in self.powerplants:
                if isinstance(pp, Windturbine):
                    if self.load > 0:
                        wind_production = pp.compute_wind_production(self.load)
                        activated_powerplant = pp.attribute_production(wind_production)
                        self.load -= wind_production
                        self.order.append(activated_powerplant)

        # Remove windturbines powerplants from powerplants list
        self.powerplants = self._remove_windturbines()

        # Compute price per mwh for every powerplant and select the cheapest
        while self.load > 0:
            cheapest_powerplant = self._find_cheapest_powerplant()
            # Finish process
            if cheapest_powerplant == []:
                break
            load_to_attribute = self._compute_load_to_give(cheapest_powerplant)
            self.order.append(
                cheapest_powerplant.attribute_production(load_to_attribute)
            )
            self.load -= cheapest_powerplant.pmax
            self.powerplants = self._remove_powerplant(cheapest_powerplant.name)
        return self.order

    def _remove_windturbines(self):
        """Filter the list of powerplants by removing the windturbines

        Returns:
            list: the filtered list of powerplants
        """
        return [pp for pp in self.powerplants if pp.type != "windturbine"]

    def _remove_powerplant(self, name):
        """Remove the selected powerplant from the powerplants list

        Args:
            name (str): name of the powerplant

        Returns:
            list: the filtered list of powerplants
        """
        return [pp for pp in self.powerplants if pp.name != name]

    def _compute_load_to_give(self, cheapest_powerplant):
        """Determine the load to be attributed to a powerplant

        Args:
            cheapest_powerplant (Powerplant): the selected powerplant

        Returns:
            int: the remaining load or the powerplant's pmax if no load is remaining
        """
        if self.load - cheapest_powerplant.pmax >= 0:
            return cheapest_powerplant.pmax
        return self.load

    def _find_cheapest_powerplant(self):
        """Find the cheapest powerplant to use

        Returns:
            Powerplant: the found powerplant or an empty list if the process is finished
        """
        result = []
        for pp in self.powerplants:
            cost_per_mwh = pp.compute_cost_per_mwh(self.load)
            pp.cost_per_mwh = cost_per_mwh
            result.append(pp)
        if len(result) > 0:
            if len(result) > 1:
                ordered_result = sorted(result, key=lambda p: p.cost_per_mwh)
                return ordered_result[0]
            return result[0]
        return []
