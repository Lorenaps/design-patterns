# Created by Lorenaps at 02/09/18
# Implementação para patos que grasnam 'Squeak'
from designPatterns.strategy.interface.quack import Quack

class QuackSqueak(Quack):
    '''
        Implementação concreta de um supertipo (Quack)
    '''

    def quack(self):
        print("Squeak!")
