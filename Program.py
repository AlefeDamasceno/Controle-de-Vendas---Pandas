import pandas as pd 
import matplotlib.pyplot as plt

dados = pd.read_excel('vendas.xlsx')

#Calcula o Total vendido 
dados['Total_venda'] = dados['Valor_Unitario'] * dados['Quantidade']

#Calcula o Lucro Unitário
dados['Lucro_Unitário'] = dados['Valor_Unitario'] - dados['Custo_Unitario']

#Calcula o Lucro por produto
dados ['Lucro_por_produto'] = (dados['Valor_Unitario'] * dados['Quantidade'])- (dados['Custo_Unitario'] * dados['Quantidade'])

#Calcula o Ticket médio
ticket_medio = dados['Valor_Unitario'].sum() / len(dados.index)

#Calcula a Margem de Lucro
margem_lucro = (dados['Lucro_por_produto'].sum() / dados['Total_venda'].sum()) * 100

#Imprime a análise dos dados
print('Resumo Da Análise:')
print(f'ticket médio: {ticket_medio} \nMargem de Lucro: {margem_lucro:.2f}% \nReceita Total = R$ {dados['Total_venda'].sum()},00 \nLucro Total: R$ {dados["Lucro_por_produto"].sum()},00 \n')

print(dados.to_string())

#Plota os gráficos de Valor Total de vendas por produto e por categoria

fig, (ax1, ax2) = plt.subplots(1,2, figsize=(14,6))

ax1.bar(dados['Produto'], dados['Total_venda'], color='lightblue')
ax1.set_title('Total de Vendas por produto', fontsize=14)
ax1.set_xlabel('Produto', fontsize=12)
ax1.set_ylabel('Valor Total de Vendas(R$)', fontsize=12)
ax1.tick_params(axis='x', rotation = 45)

vendas_categoria = dados.groupby('Categoria')['Total_venda'].sum().reset_index()
ax2.bar(vendas_categoria['Categoria'], vendas_categoria['Total_venda'], color='lightgreen')
ax2.set_title('Total de Vendas por Categoria', fontsize=14)
ax2.set_xlabel('Categoria', fontsize=12)
ax2.set_ylabel('Valor Total de Vendas(R$)', fontsize=12)
ax2.tick_params(axis='x',rotation=45)


#Imprime os gráficos
plt.tight_layout()
plt.show()