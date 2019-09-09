# Created by Lorenaps at 02/09/18
'''
    Implementação para um tipo de pato - DuckNorth
    Essa subclasse já é instanciada com implementações
    concretas para os comportamentos fly e quack porém é
    possível mudar seu comportamento em tempo de execução
    utilizando o método set_fly_behavior() da superclasse
    Duck
'''
from designPatterns.strategy.behavior.quack_squeak import QuackSqueak
from designPatterns.strategy.behavior.fly_with_wings import FlyWithWings
from designPatterns.strategy.duck import Duck


class DuckNorth(Duck):


    def __init__(self, name):
        super().__init__(FlyWithWings(), QuackSqueak(), name)
