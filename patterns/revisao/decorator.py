'''
    Usando Decorator em python: Temos uma função que permite extender
    o comportamento de um segunda função sem precisar modificar o
    código da segunda função explicitamente.

    Ele é uma função que recebe outra função como parâmentro. E para
    utilizarmos é só colocar antes da função que vai ser decorada a notação
    @nome_do_decorator

    Atenção para o retorno do decorator
'''

import time

#Função decorator
def timing_function(some_function):
    '''
        Função para
        :param some_function: função a qual queremos contabilizar o
        tempo de execução.
        :return: wrapper: função interna que contabiliza o tempo de
        execução de outra função.
    '''
    def wrapper():
        '''
            Fução para contabiliza o tempo de execução de outra função.
        '''
        start = time.time()
        some_function()
        end = time.time()
        print("Time it took to run the function: " + str((end - start)) + "\n")
    return wrapper

#Função que pode ser decorada
@timing_function
def my_function():
    '''
        Função que soma o conjunto de números gerados aleatoriamente
        e adicionados a uma lista.
    '''
    num_list = []
    for num in range(0, 10000):
        num_list.append(num)
    print("\nSum of all the numbers: " + str((sum(num_list))))

my_function()
