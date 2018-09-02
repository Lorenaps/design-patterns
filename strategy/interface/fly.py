# Created by Lorenaps at 02/09/18
'''
    Classe abstrata que representa o conceito de 'Interface'
    para o comportamento Fly
'''
import abc


class Fly(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def fly(self):
        return
