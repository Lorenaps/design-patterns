# Created by Lorenaps at 02/09/18
'''
    Classe que representa a entidade abstrata para qualquer Pato.
    Um pato possui um coportamento de voo,
    um comportamento de 'quack' e um nome.

    Os atributos comportamentos e os métodos que executam
    cada comportamento de forma encapsulada são parte da
    forma de utilizar os conceitos do padrão de projeto Strategy,
    onde adicionamos variáveis que poderão receber em tempo de
    execução qualquer que seja o comportamento desejado.

    Assim a cada novo pato nós podemos determinar a forma como
    ele se comporta na definição da sua subclasse ou em tempo
    de execução.
'''


class Duck:
    fly_behavior = None
    quack_behavior = None
    name = None


    def __init__(self, fly_behavior, quack_behavior, name):
        self.fly_behavior = fly_behavior
        self.quack_behavior = quack_behavior
        self.name = name

    def perform_fly(self):
        '''
            Princípio de programar para um supertipo
            Nesse caso você sabe que o objeto é capaz de voar,
            mas os detalhes da implementação desse voo ficam
            restritos e reutilizáveis dentro de outra classe
        '''
        self.fly_behavior.fly()

    def perform_quack(self):
        self.quack_behavior.quack()

    def display(self):
        print("I'm the duck: " + self.name)

    def set_fly_behavior(self, new_fly_behavior):
        self.fly_behavior = new_fly_behavior

    def set_quack_behavior(self, new_quack_behavior):
        self.fly_behavior = new_quack_behavior
