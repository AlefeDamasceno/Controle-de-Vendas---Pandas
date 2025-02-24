# Análise de Vendas

Este mini-projeto visa analisar dados de vendas utilizando a linguagem Python e bibliotecas como **pandas** e **matplotlib**. O objetivo principal é gerar alguns insights financeiros e visuais sobre as vendas de uma loja, a partir de um arquivo Excel.

## Descrição

O código carrega dados de vendas de um arquivo Excel e realiza os seguintes cálculos:

- **Total de Vendas**: Calcula o total gerado por cada produto.
- **Lucro Unitário**: Calcula o lucro de cada unidade de produto vendida.
- **Lucro por Produto**: Calcula o lucro total de cada produto considerando a quantidade vendida.
- **Ticket Médio**: Calcula o valor médio de cada venda.
- **Margem de Lucro**: Calcula a margem de lucro em relação ao total das vendas.

Além disso, o código gera dois gráficos:
1. **Total de Vendas por Produto**: Um gráfico de barras que mostra o total de vendas para cada produto.
2. **Total de Vendas por Categoria**: Um gráfico de barras que mostra o total de vendas por categoria de produto.

## Como Rodar

1. **Instalação das Bibliotecas Necessárias**

   Primeiro, instale as bibliotecas requeridas:

   ```bash
   pip install pandas matplotlib openpyxl
