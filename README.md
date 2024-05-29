# Orientação a Objeto e Design Patterns
Projeto criado para estudar padrões de projeto e outras aplicações na linguagem Python.

## Revisão

**Relembrando paradigmas de programação:**
> Funcional: Avaliação de funções matemáticas 'f(x) = x + 2'.

> Lógico (restritivo): Utilizado em aplicações voltadas para inteligência artificial. Se utiliza de proposições, regras de inferência e busca (estratégia para controle das inferências) ~ Lembra de prolog, meu anjo?

> Declarativo: Descrevem o que fazem e não exatamente como fazem. Linguagens de marcação são um bom exemplo.

> Imperativo (Procedimentos): Especifica em procedimentos os passos que o programa deve seguir tendo a possibilidade de chamar esses procedimentos em qualquer parte do código. O código fica separado em módulos.

> Orientado a objetos: Construção do código utilizando conceitos mais próximos do mundo real. Dividindo o sistema em um conjunto de classes que definem objetos, e esses objetos são representados com atributos (variáveis) e comportamentos (métodos).

> Orientado a eventos: Geralmente linguagens que dão suporte a interface gráfica.

**Alguns conceitos e abreviações:** 

> **Polimorfismo** significa a possibilidade de programar considerando abstrações que poderão ser especializadas quando necessário e, inclusive, intercamibadas. Programar para um supertipo é vida <3
O polimorfismo pode ser aplicado através a utilização de um supertipo ou através de herança, quando utilizamos a *sobrecarga de métodos*.

> **Overriding** - Sobrescrevendo - Quando uma classe filha tem a possibilidade de utilizar o mesmo método da classe mãe usando mesmo nome e parâmentros mas a implementação diferente.

> **Overloading** - Sobrecarregando - Quando uma classe filha tem a possibilidade de utilizar o mesmo método da classe mãe usando apenas parâmentros diferentes.

> DRY - *'Don't repeat yourself'* (todo: desenvolver)

> MRO - *'Method Resolution Order'* (todo: desenvolver)

## Design Patterns

São soluções para problemas comuns :)


### Classificação dos Padrões

#### Padrões para Criação
Organizar em um sistema. Definição e criação de um objeto.

- Factory: Define uma interface para criação de um objeto, mas adia a criação da instância para o tempo de execução.
- Abtract Factory: Provê uma interface para criar famílias de objetos relacionados sem especificar sua classe concreta.
- Builder: Busca separar a construção de um objeto complexo de sua representação, para que o mesmo processo de construção possa criar diferentes representações.
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

- Command: Permite desconectar o autor de uma solicitação do objeto que deverá executar a ação solicitada. Encapsula uma solicitação como um objeto, o que lhe permite parametrizar outros objetos com diferentes solicitações.
- State
- Chain of responsability: Cria uma cadeia de objetos que examinam sequencialmente uma solicitação. Após examinar, cada objeto pode processá-la ou passá-la adiante para o próximo objeto na cadeia.
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

- Injeção de dependência: Módulos de alto nível não devem depender de módulos de baixo nível. Ambos devem depender de abstrações. Tipo de injeção de dependência: Por construtor, por interface e por propriedades.

### Alguns Princípios

> Open-closed: Entidades devem ser abertas para extensão, mas fechadas para modificação - Eu consigo entender melhor olhando a aplicação do padrão strategy. Se vc tem uma família da patos para um jogo mas surge um novo tipo de pato que voa de uma forma diferente voce pode implementar 

> Programe para uma interface e não para uma implementação

> Entidades com responsabilidade única

> SOLID (TODO: desenvolver)


## Referências e Links Úteis

- FREEMAN, Eric; FREEMAN, E. Use a cabeça–Padrões de Projeto, 2a edição. 2009.
- [O que é um padrão de projeto? | Refactoring Guru](https://refactoring.guru/pt-br/design-patterns/what-is-pattern)
- [Design Patterns](https://www.udemy.com/python-design-patterns/) - Curso na Udemy criado por Packt Publishing
- [Linguagens e paradigmas de programação](https://www.treinaweb.com.br/blog/linguagens-e-paradigmas-de-programacao/)
- [OOP | Polimorfismo](https://deviniciative.wordpress.com/2019/08/19/oop-polimorfismo/)
- [Python e Orientação a Objetos](https://www.caelum.com.br/apostila-python-orientacao-objetos/#null)
- [Python Orientado a Objetos - Grupo Python](https://www.dcc.ufrj.br/~fabiom/mab225/pythonoo.pdf)
- [Sobre o padrão Decorator em Python](https://pythonhelp.wordpress.com/2013/06/09/entendendo-os-decorators/) - Artigo do Python Help
- [Injeção de Dependência por Eduardo Lanfredi](https://medium.com/@eduardolanfredi/inje%C3%A7%C3%A3o-de-depend%C3%AAncia-ff0372a1672)
- [Convenções de nomenclatura: Camel, Pascal, Kebab e Snake case - Alura](https://www.alura.com.br/artigos/convencoes-nomenclatura-camel-pascal-kebab-snake-case)
