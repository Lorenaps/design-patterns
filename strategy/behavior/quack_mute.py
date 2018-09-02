# Created by Lorenaps at 02/09/18
# Implementação para patos que não podem grasnar
from designPatterns.strategy.interface.quack import Quack

class QuackMute(Quack):

    def quack(self):
        print("I'm not quackable")
