# Analisador de Gastos Pessoais

Aplicativo de terminal em Python para controle de gastos pessoais,
com cadastro, edição, exclusão, filtro por categoria e persistência
de dados em arquivo JSON.

Projeto de estudo, com apoio de IA para revisão de código e boas práticas.

## Funcionalidades

- Cadastro de gastos com descrição, valor e categoria
- Listagem de todos os gastos com total geral
- Cálculo de total geral e total por categoria
- Filtro de gastos por categoria
- Edição de gastos existentes (descrição, valor ou categoria)
- Exclusão de gastos com confirmação
- Salvamento e carregamento de dados em arquivo JSON (`gastos.json`)

## Como executar

```bash
python analisador_gastos.py
```

## Exemplo de uso
MENU PRINCIPAL
Adicionar gasto
Listar todos os gastos
Ver total gasto
...
Escolha uma opção: 1
NOVO GASTO

Descrição: Mercado
Valor (R$): 150
Categoria disponíveis:

Alimentação
...
Gasto adicionado: Mercado - R$ 150.00 (Alimentação)

## Testes

```bash
python -m unittest test_analisador_gastos.py
```

## Conceitos aplicados

- Manipulação de arquivos JSON (persistência de dados)
- Estruturas de repetição e decisão
- Tratamento de exceções
- Funções auxiliares e reutilização de código
- Testes unitários
