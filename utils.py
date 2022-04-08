import enums
import tower

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
        game.ocupy_cells(map_cell, 1)
        if game.selected_tower == enums.Tower.MACHINE_GUN:
            game.towers.append(tower.MachineGun(game.bf_map, map_cell))
        elif game.selected_tower == enums.Tower.CANNON:
            game.towers.append(tower.Cannon(game.bf_map, map_cell))
        elif game.selected_tower == enums.Tower.ANTI_TANK:
            game.towers.append(tower.AntiTank(game.bf_map, map_cell))
        elif game.selected_tower == enums.Tower.MISSILE:
            game.towers.append(tower.Missile(game.bf_map, map_cell))


def select_tower(game, tower):
    """
    Selects a tower type
    """
    if game.selected_tower == tower:
        game.selected_tower = None
    else:
        game.selected_tower = tower
