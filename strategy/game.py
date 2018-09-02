# Created by Lorenaps at 02/09/18
# Script para teste da atividade sobre o padrão Strategy
from designPatterns.strategy.behavior.fly_no_way import FlyNoWay
from designPatterns.strategy.behavior.fly_with_wings import FlyWithWings
from designPatterns.strategy.duck_north import DuckNorth

NEW_DUCK = DuckNorth("Abel")
NEW_DUCK.display()
NEW_DUCK.perform_fly()
NEW_DUCK.set_fly_behavior(FlyNoWay())
NEW_DUCK.perform_fly()
NEW_DUCK.set_fly_behavior(FlyWithWings())
NEW_DUCK.perform_fly()
