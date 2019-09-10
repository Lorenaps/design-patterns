# Orientação a Objeto e Design Patterns
Projeto criado para estudar orientação a objeto e padrões de projeto na linguagem Python.

## Orientação a Objeto

**Primeiro uma revisita aos paradigmas de programação:**
> Funcional: Avaliação de funções matemáticas 'f(x) = x + 2'.

> Lógico (restritivo): Utilizado em aplicações voltadas para inteligência artificial. Se utiliza de proposições, regras de inferência e busca (estratégia para controle das inferências) ~ Lembra de prolog, meu anjo?

> Declarativo: Descrevem o que fazem e não exatamente como fazem. Linguagens de marcação são um bom exemplo.

> Imperativo (Procedimentos): Especifica em procedimentos os passos que o programa deve seguir tendo a possibilidade de chamar esses procedimentos em qualquer parte do código. O código fica separado em módulos.

> Orientado a objetos: Construção do código utilizando conceitos mais próximos do mundo real. Dividindo o sistema em um conjunto de classes que definem objetos, e esses objetos são representados com atributos (variáveis) e comportamentos (métodos).

> Orientado a eventos: Geralmente linguagens que dão suporte a interface gráfica.

Bom... já sabemos que na orientação a objetos dividimos o sistema em um conjunto de classes que vão representar atributos e métodos.
Mas pensando em Python é preciso dar uma voltinha em outros conceitos primeiro.

...

Alguns conceitos e abreviações: 

- **Polimorfismo** significa a possibilidade de programar considerando abstrações que poderão ser especializadas quando necessário e, inclusive, intercamibadas. Programar para um supertipo é vida <3
O polimorfismo pode ser aplicado através a utilização de um supertipo ou através de herança, quando utilizamos a *sobrecarga de métodos*.

- **Overriding** - Sobrescrevendo - Quando uma classe filha tem a possibilidade de utilizar o mesmo método da classe mãe usando mesmo nome e parâmentros mas a implementação diferente.

- **Overloading** - Sobrecarregando - Quando uma classe filha tem a possibilidade de utilizar o mesmo método da classe mãe usando apenas parâmentros diferentes.

- DRY - *'Don't repeat yourself'* (TODO: desenvolver)

- MRO - *'Method Resolution Order'* (TODO: desenvolver)

Referências:

- [Linguagens e paradigmas de programação](https://www.treinaweb.com.br/blog/linguagens-e-paradigmas-de-programacao/)
- [OOP | Polimorfismo](https://deviniciative.wordpress.com/2019/08/19/oop-polimorfismo/)
- [Python e Orientação a Objetos](https://www.caelum.com.br/apostila-python-orientacao-objetos/#null)

## Design Patterns

São soluções para problemas comuns :)


### Classificação dos Padrões

#### Padrões para Criação
Organizar em um sistema. Definição e criação de um objeto.

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
    Nesse caso nós não precisamos nos preocupar se o conjunto tem elementos, quantos elementos são... Internamente o 'for' sabe como percorrer aquele conjunto e o que fazer enquanto ele tiver elementos.
    
## Alguns Princípios

- Open-closed: Entidades devem ser abertas para extensão, mas fechadas para modificação.
- Programe para uma interface e não para uma implementação
- Entidades com responsabilidade única

- TODO: Estudar mais o SOLID


## Links Úteis
* [Sobre o padrão Decorator em Python](https://pythonhelp.wordpress.com/2013/06/09/entendendo-os-decorators/) - Artigo do Python Help
* [Curso na Udemy](https://www.udemy.com/python-design-patterns/) - Curso criado por Packt Publishing