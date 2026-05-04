# Validador de CPF

## Objetivo

Este projeto foi desenvolvido com a finalidade de validar um número de CPF utilizando a linguagem Python. A aplicação informa ao usuário se o CPF digitado é válido ou inválido, com base no cálculo dos dígitos verificadores.

---

## Funcionalidades

* Leitura do CPF informado pelo usuário
* Remoção automática de caracteres como pontos e traços
* Verificação se o CPF possui 11 dígitos
* Identificação de sequências inválidas (como números repetidos)
* Validação dos dígitos verificadores
* Exibição do resultado na tela

---

## Tecnologias utilizadas

* Python 3

---

## Como executar o projeto

1. Clone este repositório:

```
git clone https://github.com/viniciusalves/validar-cpf
```

2. Acesse a pasta do projeto:

```
cd validar-cpf
```

3. Execute o programa:

```
python validar_cpf.py
```

4. Digite um CPF quando solicitado e veja o resultado.

---

## Sobre o algoritmo de validação

O CPF é composto por 11 dígitos, sendo os dois últimos responsáveis por garantir a validade do número.

O processo de validação segue as seguintes etapas:

1. Remoção de todos os caracteres que não são números
2. Verificação do tamanho do CPF (11 dígitos)
3. Eliminação de casos inválidos conhecidos (como todos os dígitos iguais)
4. Cálculo do primeiro dígito verificador a partir dos 9 primeiros dígitos
5. Cálculo do segundo dígito verificador a partir dos 10 primeiros dígitos
6. Comparação dos dígitos calculados com os informados

Se os valores coincidirem, o CPF é considerado válido.

---

## Estrutura do projeto

```
validar-cpf/
│
├── validar_cpf.py
├── apresentacao.pdf (ou .pptx)
└── README.md
```

---

## Autor

Vinicius Alves

---

## Observação

Este projeto foi desenvolvido para fins acadêmicos, com o objetivo de praticar lógica de programação e compreensão de algoritmos.
