# Created by Lorenaps at 02/09/18
'''
    Classe abstrata que representa o conceito de 'Interface'
    para o comportamento Fly
'''
import abc


class Fly(metaclass=abc.ABCMeta):
    '''
        Criação de um supertipo
        No caso um supertipo para o comportamento de voar
    '''

    @abc.abstractmethod
    def fly(self):
        return