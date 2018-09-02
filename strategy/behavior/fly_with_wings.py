# Created by Lorenaps at 02/09/18
# Implementação para patos que voam com asas
from designPatterns.strategy.interface.fly import Fly


class FlyWithWings(Fly):

    def __init__(self):
        super().__init__()

    def fly(self):
        print("I'm flying with wings!")
