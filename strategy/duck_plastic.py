# Created by Lorenaps at 02/09/18
'''
    Implementação para um tipo de pato - DuckPlastic
'''
from designPatterns.strategy.behavior.fly_no_way import FlyNoWay
from designPatterns.strategy.behavior.quack_mute import QuackMute
from designPatterns.strategy.duck import Duck


class DuckPlastic(Duck):


    def __init__(self, name):
        super().__init__(FlyNoWay(), QuackMute(), name)
