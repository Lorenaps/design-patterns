# Created by Lorenaps at 02/09/18
'''
    Classe abstrata que representa o conceito de 'Interface'
    para o comportamento Quack
'''
import abc


class Quack(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def quack(self):
        return
