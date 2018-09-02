# Created by Lorenaps at 02/09/18
# Implementação para patos que não devem voar
from designPatterns.strategy.interface.fly import Fly


class FlyNoWay(Fly):

    def fly(self):
        print("I'm not flyable!")
