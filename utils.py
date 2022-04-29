import enums
import tower
import resourceFactory

def valid_index(index, list_dim):
    """
    Returns if a given index is valid
    considering a list of dimensions list_dim.
    """
    for i, ind in enumerate(index):
        if 0<= ind < list_dim[i]:
            return True
    return False


def direction2angle(direction):
    """
    Returns the angle from the direction.
    """
    if direction == enums.Direction.RIGHT:
        return 0
    elif direction == enums.Direction.UP:
        return 90
    elif direction == enums.Direction.LEFT:
        return 180
    elif direction == enums.Direction.DOWN:
        return -90

def add_tower(map_cell, game):
    """
    Adds tower to map
    """
    if game.selected_tower is None:
        return
    if game.are_cells_empty(map_cell, 1):
        if game.selected_tower == enums.Tower.MACHINE_GUN_LVL1 and game.resources >= tower.MachineGunLvl1.price:
            game.ocupy_cells(map_cell, 1)
            game.towers.append(tower.MachineGunLvl1(game.bf_map, map_cell))
            game.decrease_resources(tower.MachineGunLvl1.price)
        elif game.selected_tower == enums.Tower.CANNON_LVL1 and game.resources >= tower.CannonLvl1.price:
            game.ocupy_cells(map_cell, 1)
            game.towers.append(tower.CannonLvl1(game.bf_map, map_cell))
            game.decrease_resources(tower.CannonLvl1.price)
        elif game.selected_tower == enums.Tower.ANTI_TANK_LVL1 and game.resources >= tower.AntiTankLvl1.price:
            game.ocupy_cells(map_cell, 1)
            game.towers.append(tower.AntiTankLvl1(game.bf_map, map_cell))
            game.decrease_resources(tower.AntiTankLvl1.price)
        elif game.selected_tower == enums.Tower.MISSILE_LVL1 and game.resources >= tower.MissileLvl1.price:
            game.ocupy_cells(map_cell, 1)
            game.towers.append(tower.MissileLvl1(game.bf_map, map_cell))
            game.decrease_resources(tower.MissileLvl1.price)
        elif game.selected_tower == enums.ResourceFactory.COAL_FACTORY and game.resources >= resourceFactory.CoalFactory.price:
            game.ocupy_cells(map_cell, 1)
            game.resource_factories.append(resourceFactory.CoalFactory(game.bf_map, map_cell))
            game.decrease_resources(resourceFactory.CoalFactory.price)

def update_tower(map_cell, game):
    "Updates a tower in map"
    if not game.are_cells_empty(map_cell, 1):
        for index, curr_tower in enumerate(game.towers):
            if curr_tower.pos == map_cell and game.resources >= curr_tower.update_price:
                price = curr_tower.update_price
                if curr_tower.tower_type == enums.Tower.MACHINE_GUN_LVL1:
                    game.towers[index] = tower.MachineGunLvl2(game.bf_map, map_cell)
                elif curr_tower.tower_type == enums.Tower.MACHINE_GUN_LVL2:
                    game.towers[index] = tower.MachineGunLvl3(game.bf_map, map_cell)
                elif curr_tower.tower_type == enums.Tower.CANNON_LVL1:
                    game.towers[index] = tower.CannonLvl2(game.bf_map, map_cell)
                elif curr_tower.tower_type == enums.Tower.CANNON_LVL2:
                    game.towers[index] = tower.CannonLvl3(game.bf_map, map_cell)
                elif curr_tower.tower_type == enums.Tower.ANTI_TANK_LVL1:
                    game.towers[index] = tower.AntiTankLvl2(game.bf_map, map_cell)
                elif curr_tower.tower_type == enums.Tower.MISSILE_LVL1:
                    game.towers[index] = tower.MissileLvl2(game.bf_map, map_cell)

                game.decrease_resources(price)
                break

def update_factory(map_cell, game):
    "Updates a factory in map"
    if not game.are_cells_empty(map_cell, 1):
        for index, curr_factory in enumerate(game.resource_factories):
            if curr_factory.pos == map_cell and game.resources >= curr_factory.update_price:
                price = curr_factory.update_price
                if curr_factory.factory_type == enums.ResourceFactory.COAL_FACTORY:
                    game.resource_factories[index] = resourceFactory.NuclearPlant(game.bf_map, map_cell)
                
                game.decrease_resources(price)
                break

def select_tower(game, tower):
    """
    Selects a tower type
    """
    if game.selected_tower == tower:
        game.selected_tower = None
    else:
        game.selected_tower = tower
