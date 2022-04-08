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

def add_turret(map_cell, game):
    """
    Adds turret to map
    """
    if game.selected_tower is None:
        return
    else:
        game.towers.append(tower.MachineGun(game.bf_map, map_cell))
