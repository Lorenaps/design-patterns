Projeto criado para estudar padrões de projeto na linguagem python.

### Classificação dos Padrões

#### Criação
Organizar em um sistema definição e criação de um objeto

- Factory
- Builder
- Prototype
- Singleton
- Borg
 

#### Estrutural
Organizar relacionamentos entre entidades.

- MVC
- Facade
- Proxy
- Decorator
- Adaptor

#### Comportamento
Organização da comunicação e responsabilidade entre as entidades.

- Command
- State
- Chain of responsability
- Strategy
- Observer
- Memento

#### Anotações

- Iterator:
É um padrão já embutido na linguagem python que proporciona uma forma de acessar os elementos de um conjunto sequencial de objetos, sem precisar saber como esse elemento é representado.

    `for i in itens:
        print(i)`
    
    Nesse caso nós não precisamos nos preocupar se o conjunto tem elementos, quantos elementos são... Internamente o for sabe como percorrer aquele conjunto e o que fazer enquanto ele tiver elementos.