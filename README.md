# Estudando Design Patterns
:simple_smile:
Projeto criado para estudar padrões de projeto na linguagem python.

### Classificação dos Padrões
#### Padrões para Criação
Organizar em um sistema definição e criação de um objeto

- Factory
- Builder
- Prototype
- Singleton
- Borg

#### Padrões Estruturais
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
- Strategy: Define uma família de algoritmos, encapsula cada um deles e dispoe uma forma de deixar todos eles intercambiáveis.
- Observer
- Memento
- Iterator:
É um padrão já embutido na linguagem python que proporciona uma forma de acessar os elementos de um conjunto sequencial de objetos, sem precisar saber como esse elemento é representado.
    ```
    for i in itens:
        print(i)
    ```
    Nesse caso nós não precisamos nos preocupar se o conjunto tem elementos, quantos elementos são... Internamente o for sabe como percorrer aquele conjunto e o que fazer enquanto ele tiver elementos.
    
## Alguns Princípios

- Open-closed: Entidades devem ser abertas para extensão, mas fechadas para modificação.
- Programe para uma interface e não para uma implementação
- Entidades com responsabilidade única
- TODO: Estudar mais o SOLID


## Links Úteis
* [Sobre o padrão Decorator em Python](https://pythonhelp.wordpress.com/2013/06/09/entendendo-os-decorators/) - Artigo do Python Help
* [Curso na Udemy](https://www.udemy.com/python-design-patterns/) - Curso criado por Packt Publishing