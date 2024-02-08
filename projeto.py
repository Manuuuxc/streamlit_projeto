import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

st.markdown("<h1 style='color: blue;'>Emanuelly Conrado</h1>", unsafe_allow_html=True)


# Título do aplicativo
st.title('Meu Primeiro Projeto com Streamlit')


# importando os dados
dados = pd.read_csv('ssense_dataset.csv')


st.write('Nesse projeto vamos analisar os insights de mercado com base em gênero, segmentação de Marca e Preço e  tendências em moda de luxo')


# Título do aplicativo
st.title('Análise de Moda SSENSE')

# Subtítulo e descrição
st.subheader('As 10 Marcas de Moda de Luxo Mais Populares na SSENSE')
st.write('Esta análise mostra as 10 marcas de moda de luxo mais populares atualmente na SSENSE, com base na quantidade de produtos disponíveis.')

# Contando a quantidade de produtos por marca
contagem_por_marca = dados['brand'].value_counts().head(10)

# Criar o gráfico com Seaborn
plt.figure(figsize=(12, 6))
sns.barplot(x=contagem_por_marca.values, y=contagem_por_marca.index, palette='viridis')
plt.title('Top 10 Marcas Populares na SSENSE')
plt.xlabel('Quantidade de Produtos')
plt.ylabel('Marca')

# Mostrar o gráfico
st.pyplot()
st.set_option('deprecation.showPyplotGlobalUse', False)

# Pergunta e descrição
st.header('Quais são as 10 marcas de moda de luxo com os maiores valores de vendas no total?')
st.write('A partir dos valores totais de vendas, foi possível identificar as marcas que contribuem significativamente para o faturamento total da loja.')

# Calcular os valores totais de vendas por marca
vendas_por_marca = dados.groupby('brand')['price_usd'].sum().reset_index().sort_values(by='price_usd', ascending=False).head(10)

# Exibir as 10 marcas com maiores valores de vendas
st.write('As 10 Marcas de Moda de Luxo com os Maiores Valores de Vendas Totais na SSENSE:')
st.write(vendas_por_marca)

# Criar o gráfico com Seaborn
plt.figure(figsize=(12, 6))
sns.barplot(data=vendas_por_marca, x='price_usd', y='brand', palette='coolwarm')
plt.title('Marcas mais lucrativas em termos de vendas totais')
plt.xlabel('Valor Total de Vendas (USD)')
plt.ylabel('Marca')

# Mostrar o gráfico
st.pyplot()


# Pergunta 3: Comparação de Desempenho por Gênero
st.header('Comparação de Desempenho por Gênero')

# Calcular o faturamento total por tipo de produto
faturamento_por_genero = dados.groupby('type')['price_usd'].sum()

# Exibir o faturamento total para produtos masculinos e femininos
st.write(f"O faturamento total para produtos masculinos é de ${faturamento_por_genero['mens']:.2f}.")
st.write(f"O faturamento total para produtos femininos é de ${faturamento_por_genero['womens']:.2f}.")

# Calcular o faturamento total por tipo de produto
mas_genero = dados.groupby('type')['price_usd'].sum().reset_index().sort_values(by='price_usd', ascending=False)

# Exibir os resultados
st.write(mas_genero)

# Pergunta 4: Participação percentual de cada tipo de produto no faturamento total
st.header('Participação percentual de cada tipo de produto no faturamento total')

# Calcular a participação percentual de cada tipo
participacao_percentual = faturamento_por_genero / faturamento_por_genero.sum() * 100

# Exibir a participação percentual por tipo de produto
st.write(f"A participação percentual de faturamento total para produtos masculinos (tipo 'mens') é de aproximadamente {participacao_percentual['mens']:.2f}%, enquanto a participação para produtos femininos (tipo 'womens') é de cerca de {participacao_percentual['womens']:.2f}%.")

# Criar o gráfico de pizza
labels = participacao_percentual.index
valores = participacao_percentual.values
cores = ['gold', 'lightcoral']

plt.figure(figsize=(8, 8))
plt.pie(valores, labels=labels, colors=cores, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Participação percentual no faturamento por tipo de produto')
plt.axis('equal')

# Mostrar o gráfico
st.pyplot()

