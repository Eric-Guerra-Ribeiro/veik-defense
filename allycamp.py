import gameconstants as gc

class AllyCamp():
      def __init__(self, pos):
          self._pos = pos
          self._max_health = gc.BASE_HEALTH*20
          self.health = self._max_health
          self.alive = True
      
      def take_dmg(self, dmg):
            self.health -= dmg
            if self.health <= 0:
                  self.die()
      
      def get_health_perc(self):
            return self.health/self._max_health

      def get_pos(self):
            return self._pos
      
      def die(self):
            self.alive = False

