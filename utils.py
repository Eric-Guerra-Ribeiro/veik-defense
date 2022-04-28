import enums
import tower
import waves

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
        if game.selected_tower == enums.Tower.MACHINE_GUN and game.resources >= tower.MachineGun.price:
            game.ocupy_cells(map_cell, 1)
            game.towers.append(tower.MachineGun(game.bf_map, map_cell))
            game.decrease_resources(tower.MachineGun.price)
        elif game.selected_tower == enums.Tower.CANNON and game.resources >= tower.Cannon.price:
            game.ocupy_cells(map_cell, 1)
            game.towers.append(tower.Cannon(game.bf_map, map_cell))
            game.decrease_resources(tower.Cannon.price)
        elif game.selected_tower == enums.Tower.ANTI_TANK and game.resources >= tower.AntiTank.price:
            game.ocupy_cells(map_cell, 1)
            game.towers.append(tower.AntiTank(game.bf_map, map_cell))
            game.decrease_resources(tower.AntiTank.price)
        elif game.selected_tower == enums.Tower.MISSILE and game.resources >= tower.Missile.price:
            game.ocupy_cells(map_cell, 1)
            game.towers.append(tower.Missile(game.bf_map, map_cell))
            game.decrease_resources(tower.Missile.price)


def select_tower(game, tower):
    """
    Selects a tower type
    """
    if game.selected_tower == tower:
        game.selected_tower = None
    else:
        game.selected_tower = tower


def begin_campaign(game):
    """
    Starts the game on campaign mode
    """
    game.game_state = enums.GameState.GRACE_PERIOD
    game.waves = waves.WaveController("waves/classic.json", game)


def begin_challenge(game):
    """
    Starts the game on challenge mode
    """
    game.game_state = enums.GameState.GRACE_PERIOD
    game.waves = waves.WaveController("waves/endless.json", game)
