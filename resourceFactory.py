import abc

import enums
import gameconstants as gc


class ResourceFactory(abc.ABC):
    """
    Abstract class for resource factories.
    """

    def __init__(self, bf_map, pos):
        self.bf_map = bf_map
        self.pos = pos
        self.production_process = 0
        self.update_price = 0
        self.current_production = 0

    def produce(self):
        """
        Produces resources.
        """
        self.production_process += self.production_rate
        while self.production_process >= 1:
            self.production_process -= 1
            self.current_production += self.production_profit
    
    def collect(self):
        """
        Collects produced resources.
        """
        resources = self.current_production
        self.current_production = 0
        return resources
    
    def get_factory_type(self):
        return self.factory_type

class CoalFactory(ResourceFactory):
    """
    Coal Factory resource generation.
    """

    price = gc.BASE_PRICE
    production_profit = gc.BASE_PRODUCTION_PROFIT
    production_rate = gc.BASE_PRODUCTION_RATE

    def __init__(self, bf_map, pos):
        super().__init__(bf_map, pos)
        self.pos = pos
        self.factory_type = enums.ResourceFactory.COAL_FACTORY
        self.update_price = 5 * gc.BASE_PRICE

class NuclearPlant(ResourceFactory):
    """
    Nuclear Plant resource generation: update of Coal Factory.
    """

    production_profit = 3 * gc.BASE_PRODUCTION_PROFIT
    production_rate = gc.BASE_PRODUCTION_RATE

    def __init__(self, bf_map, pos):
        super().__init__(bf_map, pos)
        self.pos = pos
        self.production_rate = gc.BASE_PRODUCTION_RATE
        self.factory_type = enums.ResourceFactory.NUCLEAR_PLANT