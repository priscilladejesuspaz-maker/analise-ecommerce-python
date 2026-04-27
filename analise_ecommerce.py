# ===============================
# IMPORTAÇÃO DAS BIBLIOTECAS
# ===============================
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


# ===============================
# CARREGAMENTO DOS DADOS
# ===============================
# Caminho do arquivo CSV (ajuste conforme sua máquina)
df = pd.read_csv(
    'C:/Users/Book/Documents/Análise de Dados - EBAC/Python/aula_visualização_dados_python/ecommerce_estatistica.csv',
    sep=',',
    encoding='utf-8'
)

# Visualização inicial dos dados
print(df.head())
print(df.columns)

# ===============================
# TRATAMENTO DE DADOS
# ===============================
# Função para converter valores de "Qtd_Vendidos"
# Exemplo: "1.5mil" -> 1500 | "500" -> 500
def converter(valor):
    valor = valor.replace('+', '').lower()

    if 'mil' in valor:
        return float(valor.replace('mil', '')) * 1000
    else:
        return float(valor)


# Aplicando a conversão na coluna
df['Qtd_Vendidos'] = df['Qtd_Vendidos'].apply(converter)

print(df[['Preço', 'Qtd_Vendidos']].corr())

# ===============================
# 1. HISTOGRAMA
# ===============================
plt.figure(figsize=(8,5))

plt.hist(df['Qtd_Vendidos'], bins=30, color='blue', alpha=0.8)

plt.title('Distribuição da Quantidade Vendida')
plt.xlabel('Quantidade Vendida')
plt.ylabel('Frequência')
plt.grid(True)

plt.show()


# ===============================
# 2. GRÁFICO DE DISPERSÃO
# ===============================
plt.figure(figsize=(8,5))

plt.scatter(df['Preço'], df['Qtd_Vendidos'], color='#5883a8', alpha=0.6, s=30)

plt.title('Relação entre Preço e Quantidade Vendida')
plt.xlabel('Preço')
plt.ylabel('Quantidade Vendida')

plt.show()


# ===============================
# 3. GRÁFICO DE BARRAS (TOP 10 MARCAS)
# ===============================
top_marcas = (
    df.groupby('Marca')['Qtd_Vendidos']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10,5))

top_marcas.sort_values().plot(kind='barh', color='#5883a8')

plt.title('Top 10 Marcas por Quantidade Vendida')
plt.xlabel('Quantidade Vendida')
plt.ylabel('Marca')

plt.show()


# ===============================
# 4. HEATMAP (CORRELAÇÃO)
# ===============================
plt.figure(figsize=(8,5))

sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')

plt.title('Correlação entre Variáveis')

plt.show()


# ===============================
# 5. GRÁFICO DE PIZZA (TOP 5 MARCAS)
# ===============================
top_marcas_pizza = (
    df.groupby('Marca')['Qtd_Vendidos']
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

plt.figure(figsize=(6,6))

plt.pie(top_marcas_pizza, labels=top_marcas_pizza.index, autopct='%1.1f%%')

plt.title('Participação das Top 5 Marcas nas Vendas')

plt.show()

# ===============================
# 5. GRÁFICO DE DENSIDADE
# ===============================

plt.figure(figsize=(8,5))

sns.kdeplot(df['Qtd_Vendidos'], fill=True)

plt.title('Densidade da Quantidade Vendida')
plt.xlabel('Quantidade Vendida')
plt.ylabel('Densidade')

plt.show()

# ===============================
# 5. GRÁFICO DE REGRESSÃO
# ===============================

plt.figure(figsize=(8,5))

sns.regplot(x='Preço', y='Qtd_Vendidos', data=df, scatter_kws={'alpha':0.5})

plt.title('Regressão: Preço vs Quantidade Vendida')
plt.xlabel('Preço')
plt.ylabel('Quantidade Vendida')

plt.show()

