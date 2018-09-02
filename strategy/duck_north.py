# Created by Lorenaps at 02/09/18
'''
    Implementação para um tipo de pato - DuckNorth
'''
from designPatterns.strategy.behavior.quack_squeak import QuackSqueak
from designPatterns.strategy.behavior.fly_with_wings import FlyWithWings
from designPatterns.strategy.duck import Duck


class DuckNorth(Duck):


    def __init__(self, name):
        super().__init__(FlyWithWings(), QuackSqueak(), name)